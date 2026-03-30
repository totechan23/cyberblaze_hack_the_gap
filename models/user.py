# backend/models/user.py

from pydantic import BaseModel
from typing import Optional
import uuid

class User(BaseModel):
    id: str = str(uuid.uuid4())
    username: str
    password: str
    role: str  # "citizen" or "employee"

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    role: str