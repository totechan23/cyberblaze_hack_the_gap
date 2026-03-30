# backend/routes/auth.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database.db import get_db
users_db = []

router = APIRouter()

# -------------------------
# Request Models
# -------------------------

class User(BaseModel):
    username: str
    password: str
    role: str  # citizen / employee


class UserLogin(BaseModel):
    username: str
    password: str


# -------------------------
# REGISTER (Permanent)
# -------------------------

@router.post("/register")
def register(user: User, db: Session = Depends(get_db)):

    # Check if user already exists
    existing_user = db.query(UserDB).filter(
        UserDB.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    # Create new user
    new_user = UserDB(
        username=user.username,
        password=user.password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


# -------------------------
# LOGIN (Database-based)
# -------------------------

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(UserDB).filter(
        UserDB.username == user.username,
        UserDB.password == user.password
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "message": "Login successful",
        "role": db_user.role
    }