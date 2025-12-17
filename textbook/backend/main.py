"""
FastAPI Main Application
RAG Chatbot Backend with session management, text-selection queries, and CORS
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from sqlalchemy import text

from database import init_db, get_db, ChatSession, ChatMessage, UserProfile
from rag import RAGEngine
from auth import router as auth_router
from personalization import PersonalizationService
from translation import TranslationService  # Using deep-translator (Python 3.13 compatible)

load_dotenv()

# Validate required environment variables
def validate_environment():
    """Validate all required environment variables are set"""
    required_vars = {
        "OPENAI_API_KEY": "OpenRouter API key",
        "OPENAI_BASE_URL": "OpenRouter base URL",
        "QDRANT_URL": "Qdrant cluster URL",
        "QDRANT_API_KEY": "Qdrant API key",
        "DATABASE_URL": "Neon database connection string"
    }
    
    missing_vars = []
    for var, description in required_vars.items():
        value = os.getenv(var)
        if not value:
            missing_vars.append(f"  • {var} ({description})")
        elif "your_" in value or "placeholder" in value:
            missing_vars.append(f"  • {var} ({description}) - has placeholder value")
    
    if missing_vars:
        print("\n" + "="*60)
        print("❌ CONFIGURATION ERROR")
        print("="*60)
        print("\nMissing or invalid environment variables:")
        for var in missing_vars:
            print(var)
        print("\nPlease check your backend/.env file and ensure all")
        print("required variables are set with valid values.")
        print("="*60 + "\n")
        raise ValueError("Missing required environment variables")

# Validate environment on startup
validate_environment()

# Initialize FastAPI app
app = FastAPI(
    title="Physical AI Textbook RAG Chatbot",
    description="AI-powered chatbot for the Physical AI & Humanoid Robotics textbook",
    version="1.0.0"
)

# CORS configuration
allowed_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database
init_db()

# Initialize RAG engine
rag_engine = RAGEngine()

# Initialize bonus features
personalization_service = PersonalizationService()
translation_service = TranslationService()  # Using deep-translator

# Include authentication router
app.include_router(auth_router)

# Pydantic models for API

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    message: str
    selected_text: Optional[str] = None  # For text-selection based queries
    user_id: Optional[str] = None  # For personalization
    software_background: Optional[str] = 'intermediate'  # beginner/intermediate/advanced
    hardware_background: Optional[str] = 'beginner'  # beginner/intermediate/advanced

class ChatResponse(BaseModel):
    session_id: str
    message: str
    sources: List[str]
    timestamp: str

class SessionResponse(BaseModel):
    session_id: str
    created_at: str

# API Endpoints

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Physical AI Textbook RAG Chatbot",
        "version": "1.0.0"
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    """
    Main chat endpoint
    Supports both regular queries and text-selection based queries
    """
    try:
        # Get or create session
        session_id = request.session_id
        if not session_id:
            session_id = str(uuid.uuid4())
            new_session = ChatSession(id=session_id)
            db.add(new_session)
            db.commit()
        
        # Get chat history for this session
        history_messages = db.query(ChatMessage).filter(
            ChatMessage.session_id == session_id
        ).order_by(ChatMessage.created_at).all()
        
        chat_history = [
            {"role": msg.role, "content": msg.content}
            for msg in history_messages
        ]
        
        # Store user message
        user_message = ChatMessage(
            session_id=session_id,
            role="user",
            content=request.message,
            selected_text=request.selected_text
        )
        db.add(user_message)
        db.commit()
        
        # Personalize the query if user background is provided
        query_to_use = request.message
        if request.software_background and request.hardware_background:
            query_to_use = personalization_service.personalize_prompt(
                original_query=request.message,
                software_background=request.software_background,
                hardware_background=request.hardware_background
            )
        
        # Generate RAG response
        rag_response = rag_engine.query(
            question=query_to_use,
            chat_history=chat_history,
            selected_text=request.selected_text
        )
        
        # Store assistant response
        assistant_message = ChatMessage(
            session_id=session_id,
            role="assistant",
            content=rag_response["answer"],
            context_used=str(rag_response["contexts"][:2])  # Store top 2 contexts
        )
        db.add(assistant_message)
        db.commit()
        
        return ChatResponse(
            session_id=session_id,
            message=rag_response["answer"],
            sources=rag_response["sources"],
            timestamp=datetime.utcnow().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@app.post("/session/new", response_model=SessionResponse)
async def create_session(db: Session = Depends(get_db)):
    """Create a new chat session"""
    try:
        session_id = str(uuid.uuid4())
        new_session = ChatSession(id=session_id)
        db.add(new_session)
        db.commit()
        
        return SessionResponse(
            session_id=session_id,
            created_at=new_session.created_at.isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating session: {str(e)}")

@app.get("/session/{session_id}/history")
async def get_session_history(session_id: str, db: Session = Depends(get_db)):
    """Get chat history for a session"""
    try:
        messages = db.query(ChatMessage).filter(
            ChatMessage.session_id == session_id
        ).order_by(ChatMessage.created_at).all()
        
        return {
            "session_id": session_id,
            "messages": [
                {
                    "role": msg.role,
                    "content": msg.content,
                    "timestamp": msg.created_at.isoformat(),
                    "selected_text": msg.selected_text
                }
                for msg in messages
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching history: {str(e)}")

@app.delete("/session/{session_id}")
async def delete_session(session_id: str, db: Session = Depends(get_db)):
    """Delete a chat session and its messages"""
    try:
        # Delete messages
        db.query(ChatMessage).filter(ChatMessage.session_id == session_id).delete()
        # Delete session
        db.query(ChatSession).filter(ChatSession.id == session_id).delete()
        db.commit()
        
        return {"message": "Session deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting session: {str(e)}")

@app.post("/translate")
async def translate_content(text: str):
    """Translate content to Urdu using deep-translator"""
    try:
        # Use actual translation service
        translated = await translation_service.translate_to_urdu(text)
        return {
            "translated_text": translated,
            "original_text": text
        }
    except Exception as e:
        print(f"Translation error: {e}")
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    """Detailed health check for all services"""
    health_status = {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "services": {}
    }
    
    # Check Qdrant connection
    try:
        collections = rag_engine.qdrant_client.get_collections()
        collection_name = os.getenv("QDRANT_COLLECTION_NAME", "physical_ai_textbook")
        collection_names = [c.name for c in collections.collections]
        
        if collection_name in collection_names:
            collection_info = rag_engine.qdrant_client.get_collection(collection_name)
            points_count = collection_info.points_count
            health_status["services"]["qdrant"] = {
                "status": "healthy",
                "collection": collection_name,
                "points": points_count,
                "warning": "Low point count" if points_count < 100 else None
            }
        else:
            health_status["services"]["qdrant"] = {
                "status": "warning",
                "message": f"Collection '{collection_name}' not found. Run embeddings.py"
            }
    except Exception as e:
        health_status["services"]["qdrant"] = {
            "status": "unhealthy",
            "error": str(e)
        }
        health_status["status"] = "degraded"
    
    # Check database connection
    try:
        db.execute(text("SELECT 1"))
        health_status["services"]["database"] = {"status": "healthy"}
    except Exception as e:
        health_status["services"]["database"] = {
            "status": "unhealthy",
            "error": str(e)
        }
        health_status["status"] = "degraded"
    
    # Check LLM configuration
    llm_model = os.getenv("LLM_MODEL")
    health_status["services"]["llm"] = {
        "status": "configured",
        "model": llm_model
    }
    
    return health_status

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)
