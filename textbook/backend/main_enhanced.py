"""
FastAPI Main Application - Extended with Bonus Features
RAG Chatbot Backend with authentication, personalization, and translation
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

from database import init_db, get_db, ChatSession, ChatMessage, UserProfile
from rag import RAGEngine
from auth import router as auth_router
from personalization import PersonalizationService
from translation import TranslationService

load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Physical AI Textbook RAG Chatbot",  
    description="AI-powered chatbot with authentication, personalization, and translation",
    version="2.0.0"
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

# Initialize RAG engine and bonus features
rag_engine = RAGEngine()
personalization_service = PersonalizationService()
translation_service = TranslationService()

# Include authentication router
app.include_router(auth_router)

# Pydantic models for API

class ChatRequest(BaseModel):
    session_id: Optional[str] = None
    user_id: Optional[str] = None  # For personalization
    message: str
    selected_text: Optional[str] = None
    language: Optional[str] = "en"  # en or ur

class ChatResponse(BaseModel):
    session_id: str  
    message: str
    sources: List[str]
    timestamp: str

class PersonalizedIntroRequest(BaseModel):
    user_id: str
    chapter_title: str

class TranslationRequest(BaseModel):
    text: str
    target_language: str = "ur"

# API Endpoints

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Physical AI Textbook RAG Chatbot",
        "version": "2.0.0",
        "features": ["RAG", "Authentication", "Personalization", "Translation"]
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    """
    Enhanced chat endpoint with personalization support
    """
    try:
        # Get or create session
        session_id = request.session_id
        if not session_id:
            session_id = str(uuid.uuid4())
            new_session = ChatSession(
                id=session_id,
                user_id=request.user_id
            )
            db.add(new_session)
            db.commit()
        
        # Get user profile for personalization
        user_profile = None
        if request.user_id:
            user_profile = db.query(UserProfile).filter(
                UserProfile.id == request.user_id
            ).first()
        
        # Get chat history
        history_messages = db.query(ChatMessage).filter(
            ChatMessage.session_id == session_id
        ).order_by(ChatMessage.created_at).all()
        
        chat_history = [
            {"role": msg.role, "content": msg.content}
            for msg in history_messages
        ]
        
        # Personalize query if user profile exists
        query = request.message
        if user_profile:
            query = personalization_service.personalize_prompt(
                request.message,
                user_profile.software_background,
                user_profile.hardware_background
            )
        
        # Store user message
        user_message = ChatMessage(
            session_id=session_id,
            role="user",
            content=request.message,
            selected_text=request.selected_text
        )
        db.add(user_message)
        db.commit()
        
        # Generate RAG response
        rag_response = rag_engine.query(
            question=query,
            chat_history=chat_history,
            selected_text=request.selected_text
        )
        
        answer = rag_response["answer"]
        
        # Translate if requested
        if request.language == "ur":
            answer = await translation_service.translate_to_urdu(answer)
        
        # Store assistant response
        assistant_message = ChatMessage(
            session_id=session_id,
            role="assistant",
            content=answer,
            context_used=str(rag_response["contexts"][:2])
        )
        db.add(assistant_message)
        db.commit()
        
        return ChatResponse(
            session_id=session_id,
            message=answer,
            sources=rag_response["sources"],
            timestamp=datetime.utcnow().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@app.post("/personalize/intro")
async def get_personalized_intro(
    request: PersonalizedIntroRequest,
    db: Session = Depends(get_db)
):
    """Get personalized chapter introduction"""
    user = db.query(UserProfile).filter(UserProfile.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    intro = personalization_service.get_chapter_intro(
        request.chapter_title,
        user.software_background,
        user.hardware_background
    )
    
    return intro

@app.post("/translate")
async def translate_content(request: TranslationRequest):
    """Translate content to Urdu"""
    try:
        translated = await translation_service.translate_to_urdu(request.text)
        return {
            "original": request.text,
            "translated": translated,
            "language": "ur"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@app.post("/session/new")
async def create_session(
    user_id: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Create a new chat session"""
    try:
        session_id = str(uuid.uuid4())
        new_session = ChatSession(
            id=session_id,
            user_id=user_id
        )
        db.add(new_session)
        db.commit()
        
        return {
            "session_id": session_id,
            "created_at": new_session.created_at.isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating session: {str(e)}")

@app.get("/session/{session_id}/history")
async def get_session_history(session_id: str, db: Session = Depends(get_db)):
    """Get chat history for a session"""
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

@app.get("/health")
async def health_check():
    """Detailed health check"""
    try:
        collections = rag_engine.qdrant_client.get_collections()
        qdrant_status = "healthy"
    except:
        qdrant_status = "unhealthy"
    
    return {
        "status": "healthy",
        "qdrant": qdrant_status,
        "features": {
            "authentication": True,
            "personalization": True,
            "translation": True,
            "rag": True
        },
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host=host, port=port)
