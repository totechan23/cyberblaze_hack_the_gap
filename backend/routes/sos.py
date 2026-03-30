# backend/routes/sos.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SOSRequest(BaseModel):
    user: str
    location: str

@router.post("/trigger")
def trigger_sos(req: SOSRequest):
    # For hackathon: simulate SOS
    return {
        "message": f"SOS triggered for {req.user} 🚨",
        "location": req.location,
        "status": "Emergency services notified"
    }