"""
Database models and configuration for the RAG Chatbot
Uses Neon Serverless Postgres for storing chat sessions and messages
"""

from sqlalchemy import create_engine, Column, String, Integer, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models

class ChatSession(Base):
    """Stores chat session information"""
    __tablename__ = "chat_sessions"
    
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    title = Column(String, nullable=True)

class ChatMessage(Base):
    """Stores individual messages in a chat"""
    __tablename__ = "chat_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    role = Column(String)  # 'user' or 'assistant'
    content = Column(Text)
    context_used = Column(Text, nullable=True)  # RAG context that was used
    created_at = Column(DateTime, default=datetime.utcnow)
    selected_text = Column(Text, nullable=True)  # For text-selection based queries

class UserProfile(Base):
    """Stores user profiles for personalization (bonus feature)"""
    __tablename__ = "user_profiles"
    
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    name = Column(String, nullable=True)
    password_hash = Column(String, nullable=False)  # For authentication
    software_background = Column(String, nullable=True)  # beginner/intermediate/advanced
    hardware_background = Column(String, nullable=True)  # beginner/intermediate/advanced
    created_at = Column(DateTime, default=datetime.utcnow)

# Database initialization
def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Dependency for FastAPI to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
