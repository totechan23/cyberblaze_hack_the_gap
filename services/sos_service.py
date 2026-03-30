# backend/services/sos_service.py

def trigger_sos(user: str, location: str):
    # For now simulate
    return {
        "message": f"SOS triggered for {user}",
        "location": location,
        "status": "Emergency alert sent 🚨"
    }