# backend/routes/auth.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Fake DB (replace later)
users_db = []

class User(BaseModel):
    username: str
    password: str
    role: str  # "citizen" or "employee"

@router.post("/register")
def register(user: User):
    users_db.append(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: User):
    for u in users_db:
        if u["username"] == user.username and u["password"] == user.password:
            return {"message": "Login successful", "role": u["role"]}
    raise HTTPException(status_code=401, detail="Invalid credentials")