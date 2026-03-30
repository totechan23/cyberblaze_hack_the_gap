# backend/models/complaint.py

from pydantic import BaseModel
from typing import Optional
import uuid

class Complaint(BaseModel):
    id: str = str(uuid.uuid4())
    user: str
    text: str
    location: str
    
    status: str = "Pending"
    priority: str = "Medium"

class ComplaintCreate(BaseModel):
    user: str
    text: str
    location: str

class ComplaintUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None