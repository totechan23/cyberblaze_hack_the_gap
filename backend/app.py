# backend/app.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import config

# Import routes (we will create these next)
# from routes import auth, complaint, sos, ai, employee

app = FastAPI(
    title=config.APP_NAME,
    debug=config.DEBUG
)

# Enable CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------
# Root Endpoint
# ------------------------------
@app.get("/")
def home():
    return {
        "message": "AI Civic Assistant Backend Running 🚀"
    }

# ------------------------------
# Health Check
# ------------------------------
@app.get("/health")
def health_check():
    return {
        "status": "OK"
    }

# ------------------------------
# Placeholder Routes (temp)
# ------------------------------

@app.get("/test-ai")
def test_ai():
    return {"response": "AI working (placeholder)"}

@app.get("/test-complaint")
def test_complaint():
    return {"message": "Complaint route working"}

@app.get("/test-sos")
def test_sos():
    return {"message": "SOS route working 🚨"}

@app.get("/test-employee")
def test_employee():
    return {"message": "Employee dashboard route working"}

# ------------------------------
# Future Route Includes
# ------------------------------
# app.include_router(auth.router, prefix="/auth")
# app.include_router(complaint.router, prefix="/complaint")
# app.include_router(sos.router, prefix="/sos")
# app.include_router(ai.router, prefix="/ai")
# app.include_router(employee.router, prefix="/employee")