

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Message(BaseModel):
    text: str

def detect_intent(text: str):
    text = text.lower()
    
    if "help" in text or "unsafe" in text or "danger" in text:
        return "SOS"
    elif "not working" in text or "issue" in text or "problem" in text:
        return "Complaint"
    else:
        return "Query"

def detect_emotion(text: str):
    if "scared" in text or "afraid" in text:
        return "Fear"
    return "Normal"

@router.post("/process")
def process_message(msg: Message):
    intent = detect_intent(msg.text)
    emotion = detect_emotion(msg.text)

    return {
        "intent": intent,
        "emotion": emotion,
        "message": msg.text
    }