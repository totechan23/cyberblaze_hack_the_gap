# backend/services/routing.py

def route_department(text: str):
    text = text.lower()

    if "water" in text:
        return "Water Department"
    elif "electric" in text or "light" in text:
        return "Electricity Department"
    elif "road" in text:
        return "Municipal Department"
    else:
        return "General Department"