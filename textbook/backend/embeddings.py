"""
Document Embedding Pipeline
Processes markdown files, chunks them, generates embeddings, and stores in Qdrant
"""

import os
import glob
from pathlib import Path
from typing import List, Dict
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from openai import OpenAI
from dotenv import load_dotenv
import hashlib

load_dotenv()

class DocumentEmbedder:
    def __init__(self):
        self.qdrant_url = os.getenv("QDRANT_URL")
        self.qdrant_api_key = os.getenv("QDRANT_API_KEY")
        self.collection_name = os.getenv("QDRANT_COLLECTION_NAME", "physical_ai_textbook")
        
        # Initialize Qdrant client
        self.qdrant_client = QdrantClient(
            url=self.qdrant_url,
            api_key=self.qdrant_api_key
        )
        
        # Initialize OpenAI client (via OpenRouter)
        self.openai_client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL")
        )
        
        self.embedding_model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
        self.chunk_size = int(os.getenv("CHUNK_SIZE", 1000))
        self.chunk_overlap = int(os.getenv("CHUNK_OVERLAP", 200))
    
    def create_collection_if_not_exists(self, vector_size: int = 1536):
        """Create Qdrant collection if it doesn't exist"""
        try:
            collections = self.qdrant_client.get_collections().collections
            collection_names = [c.name for c in collections]
            
            if self.collection_name not in collection_names:
                self.qdrant_client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
                )
                print(f"Created collection: {self.collection_name}")
            else:
                print(f"Collection {self.collection_name} already exists")
        except Exception as e:
            print(f"Error creating collection: {e}")
    
    def chunk_text(self, text: str, metadata: Dict) -> List[Dict]:
        """Split text into overlapping chunks"""
        chunks = []
        words = text.split()
        
        for i in range(0, len(words), self.chunk_size - self.chunk_overlap):
            chunk_words = words[i:i + self.chunk_size]
            chunk_text = ' '.join(chunk_words)
            
            if chunk_text.strip():
                chunks.append({
                    "text": chunk_text,
                    "metadata": {
                        **metadata,
                        "chunk_index": len(chunks)
                    }
                })
        
        return chunks
    
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding for a text using OpenAI API"""
        try:
            response = self.openai_client.embeddings.create(
                model=self.embedding_model,
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"Error generating embedding: {e}")
            return []
    
    def process_markdown_file(self, file_path: str) -> List[Dict]:
        """Process a single markdown file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata from file path
        path_parts = Path(file_path).parts
        relative_path = str(Path(*path_parts[-3:]))  # Get last 3 parts
        
        # Create metadata
        metadata = {
            "file_path": relative_path,
            "file_name": Path(file_path).name,
            "source": "Physical AI & Humanoid Robotics Textbook"
        }
        
        # Extract module/section from path
        if "module1" in file_path:
            metadata["module"] = "Module 1: ROS 2"
        elif "module2" in file_path:
            metadata["module"] = "Module 2: Gazebo & Unity"
        elif "module3" in file_path:
            metadata["module"] = "Module 3: NVIDIA Isaac"
        elif "module4" in file_path:
            metadata["module"] = "Module 4: Vision-Language-Action"
        
        # Chunk the content
        chunks = self.chunk_text(content, metadata)
        return chunks
    
    def embed_and_store(self, docs_dir: str):
        """Process all markdown files and store in Qdrant"""
        # Create collection
        self.create_collection_if_not_exists()
        
        # Find all markdown files
        md_files = glob.glob(f"{docs_dir}/**/*.md", recursive=True)
        print(f"Found {len(md_files)} markdown files")
        
        all_points = []
        point_id = 0
        
        for file_path in md_files:
            print(f"Processing: {file_path}")
            chunks = self.process_markdown_file(file_path)
            
            for chunk in chunks:
                # Generate embedding
                embedding = self.generate_embedding(chunk["text"])
                
                if embedding:
                    # Create point
                    point = PointStruct(
                        id=point_id,
                        vector=embedding,
                        payload={
                            "text": chunk["text"],
                            **chunk["metadata"]
                        }
                    )
                    all_points.append(point)
                    point_id += 1
        
        # Batch upload to Qdrant
        if all_points:
            batch_size = 100
            for i in range(0, len(all_points), batch_size):
                batch = all_points[i:i + batch_size]
                self.qdrant_client.upsert(
                    collection_name=self.collection_name,
                    points=batch
                )
                print(f"Uploaded batch {i // batch_size + 1}")
            
            print(f"✅ Successfully embedded and stored {len(all_points)} chunks")
        else:
            print("❌ No chunks to upload")

if __name__ == "__main__":
    # Run embedding process
    docs_directory = "../docs"  # Adjust path as needed
    embedder = DocumentEmbedder()
    embedder.embed_and_store(docs_directory)
