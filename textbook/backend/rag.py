"""
RAG (Retrieval-Augmented Generation) Logic
Handles query embedding, similarity search, context assembly, and LLM response generation
"""

import os
from typing import List, Dict, Optional
from qdrant_client import QdrantClient
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class RAGEngine:
    def __init__(self):
        # Initialize Qdrant client
        self.qdrant_client = QdrantClient(
            url=os.getenv("QDRANT_URL"),
            api_key=os.getenv("QDRANT_API_KEY")
        )
        
        # Initialize OpenAI client (via OpenRouter)
        self.openai_client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL")
        )
        
        self.collection_name = os.getenv("QDRANT_COLLECTION_NAME", "physical_ai_textbook")
        self.embedding_model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
        self.llm_model = os.getenv("LLM_MODEL", "openai/gpt-3.5-turbo")
        self.top_k = int(os.getenv("TOP_K_RESULTS", 5))
        self.temperature = float(os.getenv("TEMPERATURE", 0.7))
        self.max_tokens = int(os.getenv("MAX_TOKENS", 500))
    
    def generate_query_embedding(self, query: str) -> List[float]:
        """Generate embedding for user query"""
        try:
            response = self.openai_client.embeddings.create(
                model=self.embedding_model,
                input=query
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"Error generating query embedding: {e}")
            return []
    
    def retrieve_relevant_context(self, query: str, selected_text: Optional[str] = None) -> List[Dict]:
        """
        Retrieve relevant context from Qdrant
        If selected_text is provided, prioritize context related to it
        """
        # If user selected specific text, use that as additional context
        search_query = query
        if selected_text:
            search_query = f"{selected_text}\n\nQuestion: {query}"
        
        # Generate embedding for the query
        query_embedding = self.generate_query_embedding(search_query)
        
        if not query_embedding:
            return []
        
        # Search in Qdrant
        try:
            search_result = self.qdrant_client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=self.top_k,
                with_payload=True
            )
            
            # Format results
            contexts = []
            for hit in search_result:
                contexts.append({
                    "text": hit.payload.get("text", ""),
                    "metadata": {
                        "file_name": hit.payload.get("file_name", ""),
                        "module": hit.payload.get("module", ""),
                        "score": hit.score
                    }
                })
            
            return contexts
        
        except Exception as e:
            print(f"Error retrieving context: {e}")
            return []
    
    def generate_response(
        self, 
        query: str, 
        contexts: List[Dict],
        chat_history: Optional[List[Dict]] = None,
        selected_text: Optional[str] = None
    ) -> Dict:
        """Generate response using LLM with retrieved context"""
        
        # Build context string from retrieved chunks
        context_str = "\n\n---\n\n".join([
            f"Source: {ctx['metadata'].get('file_name', 'Unknown')}\n{ctx['text']}"
            for ctx in contexts
        ])
        
        # Build system prompt
        system_prompt = """You are an expert AI assistant for the Physical AI & Humanoid Robotics textbook. 
Your role is to help students learn about robotics, ROS 2, simulation, NVIDIA Isaac, and Vision-Language-Action systems.

Guidelines:
1. Answer questions based on the provided textbook context
2. Be clear, concise, and educational
3. Use examples when helpful
4. If the context doesn't contain the answer, say so honestly
5. Reference specific modules or sections when relevant
6. For code questions, provide practical examples
7. Encourage hands-on learning"""

        # Add selected text context if available
        if selected_text:
            system_prompt += f"\n\nThe user has selected this specific text from the book:\n{selected_text}\n\nAnswer their question with this context in mind."
        
        # Build messages for OpenAI
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add chat history if available
        if chat_history:
            for msg in chat_history[-5:]:  # Last 5 messages for context
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })
        
        # Add current query with context
        user_message = f"""Context from the textbook:
{context_str}

Question: {query}"""
        
        messages.append({"role": "user", "content": user_message})
        
        # Generate response
        try:
            response = self.openai_client.chat.completions.create(
                model=self.llm_model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            answer = response.choices[0].message.content
            
            return {
                "answer": answer,
                "contexts": contexts,
                "sources": [ctx['metadata'].get('file_name', 'Unknown') for ctx in contexts]
            }
        
        except Exception as e:
            print(f"Error generating response: {e}")
            return {
                "answer": "I apologize, but I encountered an error generating a response. Please try again.",
                "contexts": [],
                "sources": []
            }
    
    def query(
        self, 
        question: str,
        chat_history: Optional[List[Dict]] = None,
        selected_text: Optional[str] = None
    ) -> Dict:
        """
        Main RAG query function
        1. Retrieve relevant context
        2. Generate response with LLM
        """
        # Retrieve relevant context
        contexts = self.retrieve_relevant_context(question, selected_text)
        
        # Generate response
        response = self.generate_response(
            question,
            contexts,
            chat_history,
            selected_text
        )
        
        return response
