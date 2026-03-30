# backend/utils/helpers.py

import uuid
from datetime import datetime


# -------------------------
# Generate Unique ID
# -------------------------
def generate_id():
    return str(uuid.uuid4())


# -------------------------
# Current Timestamp
# -------------------------
def current_time():
    return datetime.utcnow().isoformat()


# -------------------------
# Basic Text Cleaner
# -------------------------
def clean_text(text: str):
    return text.strip().lower()


# -------------------------
# Simple Keyword Checker
# -------------------------
def contains_keywords(text: str, keywords: list):
    text = text.lower()
    return any(word in text for word in keywords)


# -------------------------
# Response Formatter
# -------------------------
def format_response(message: str, data=None):
    return {
        "message": message,
        "data": data,
        "timestamp": current_time()
    }
