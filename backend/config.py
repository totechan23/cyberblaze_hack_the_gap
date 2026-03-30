# backend/config.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # App settings
    APP_NAME = "AI Civic Assistant"
    DEBUG = True

    # OpenAI (optional for advanced AI)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    # Twilio (SOS system)
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "")

    # Database (for now simple SQLite)
    DATABASE_URL = "sqlite:///./civic.db"

    # Secret key (for auth later)
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

config = Config()
