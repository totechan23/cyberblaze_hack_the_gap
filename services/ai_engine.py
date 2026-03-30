# backend/services/ai_engine.py

def detect_intent(text: str):
    text = text.lower()

    if any(word in text for word in ["help", "unsafe", "danger", "emergency"]):
        return "SOS"
    elif any(word in text for word in ["not working", "issue", "problem", "complaint", "leak"]):
        return "Complaint"
    else:
        return "Query"


def detect_emotion(text: str):
    text = text.lower()

    if any(word in text for word in ["scared", "afraid", "panic", "help me"]):
        return "Fear"
    return "Normal"


def process_text(text: str):
    intent = detect_intent(text)
    emotion = detect_emotion(text)

    return {
        "intent": intent,
        "emotion": emotion
    }