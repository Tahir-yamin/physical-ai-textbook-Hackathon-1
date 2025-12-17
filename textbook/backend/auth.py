"""
Authentication module using better-auth
Handles user signup, signin, and profile management
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from typing import Optional
import bcrypt
import uuid
from datetime import datetime

from database import get_db, UserProfile

router = APIRouter(prefix="/auth", tags=["authentication"])

# Request/Response Models

class SignupRequest(BaseModel):
    email: EmailStr
    name: str
    password: str
    software_background: str  # beginner/intermediate/advanced
    hardware_background: str  # beginner/intermediate/advanced

class SigninRequest(BaseModel):
    email: EmailStr
    password: str

class AuthResponse(BaseModel):
    user_id: str
    email: str
    name: str
    software_background: str
    hardware_background: str
    token: str

class ProfileResponse(BaseModel):
    user_id: str
    email: str
    name: str
    software_background: str
    hardware_background: str

# Helper Functions

def hash_password(password: str) -> str:
    """Hash password using bcrypt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    """Verify password against hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def generate_token() -> str:
    """Generate a simple session token"""
    return str(uuid.uuid4())

# API Endpoints

@router.post("/signup", response_model=AuthResponse)
async def signup(request: SignupRequest, db: Session = Depends(get_db)):
    """
    User signup with background information collection
    Collects software and hardware experience for personalization
    """
    # Check if user already exists
    existing_user = db.query(UserProfile).filter(UserProfile.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Validate background levels
    valid_levels = ["beginner", "intermediate", "advanced"]
    if request.software_background not in valid_levels or request.hardware_background not in valid_levels:
        raise HTTPException(
            status_code=400,
            detail="Background levels must be: beginner, intermediate, or advanced"
        )
    
    # Create new user
    user_id = str(uuid.uuid4())
    hashed_pw = hash_password(request.password)
    
    new_user = UserProfile(
        id=user_id,
        email=request.email,
        name=request.name,
        password_hash=hashed_pw,
        software_background=request.software_background,
        hardware_background=request.hardware_background,
        created_at=datetime.utcnow()
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    # Generate session token
    token = generate_token()
    
    return AuthResponse(
        user_id=user_id,
        email=request.email,
        name=request.name,
        software_background=request.software_background,
        hardware_background=request.hardware_background,
        token=token
    )

@router.post("/signin", response_model=AuthResponse)
async def signin(request: SigninRequest, db: Session = Depends(get_db)):
    """User signin"""
    # Find user
    user = db.query(UserProfile).filter(UserProfile.email == request.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Verify password
    if not verify_password(request.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Generate token
    token = generate_token()
    
    return AuthResponse(
        user_id=user.id,
        email=user.email,
        name=user.name,
        software_background=user.software_background,
        hardware_background=user.hardware_background,
        token=token
    )

@router.get("/profile/{user_id}", response_model=ProfileResponse)
async def get_profile(user_id: str, db: Session = Depends(get_db)):
    """Get user profile"""
    user = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return ProfileResponse(
        user_id=user.id,
        email=user.email,
        name=user.name,
        software_background=user.software_background,
        hardware_background=user.hardware_background
    )

@router.put("/profile/{user_id}")
async def update_profile(
    user_id: str,
    software_background: Optional[str] = None,
    hardware_background: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Update user background preferences"""
    user = db.query(UserProfile).filter(UserProfile.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if software_background:
        user.software_background = software_background
    if hardware_background:
        user.hardware_background = hardware_background
    
    db.commit()
    
    return {"message": "Profile updated successfully"}
