# backend/models/sos.py

from pydantic import BaseModel
import uuid

class SOS(BaseModel):
    id: str = str(uuid.uuid4())
    user: str
    location: str
    message: str = "Emergency Alert"

class SOSRequest(BaseModel):
    user: str
    location: str
    