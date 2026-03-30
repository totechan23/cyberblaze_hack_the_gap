

from fastapi import APIRouter
from pydantic import BaseModel
import uuid

router = APIRouter()

complaints_db = []

class Complaint(BaseModel):
    user: str
    text: str
    location: str

@router.post("/create")
def create_complaint(comp: Complaint):
    complaint_id = str(uuid.uuid4())

    new_complaint = {
        "id": complaint_id,
        "user": comp.user,
        "text": comp.text,
        "location": comp.location,
        "status": "Pending",
        "priority": "Medium"
    }

    complaints_db.append(new_complaint)

    return {
        "message": "Complaint registered",
        "complaint_id": complaint_id
    }

@router.get("/all")
def get_all_complaints():
    return complaints_db
