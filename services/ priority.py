# backend/services/priority.py

def get_priority(text: str, emotion: str):
    text = text.lower()

    if "gas leak" in text or "fire" in text:
        return "High"
    elif emotion == "Fear":
        return "High"
    elif "not working" in text:
        return "Medium"
    else:
        return "Low"