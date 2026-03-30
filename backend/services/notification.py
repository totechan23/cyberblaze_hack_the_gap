# backend/services/notification.py

def send_notification(message: str):
    # Simulated notification
    print(f"[NOTIFICATION]: {message}")
    return {"status": "Notification sent"}