from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import config

# 👇 ADD THIS
from routes import auth, complaint, sos, ai, employee

app = FastAPI(title=config.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

# 👇 ADD THIS AT BOTTOM
app.include_router(auth.router, prefix="/auth")
app.include_router(complaint.router, prefix="/complaint")
app.include_router(sos.router, prefix="/sos")
app.include_router(ai.router, prefix="/ai")
app.include_router(employee.router, prefix="/employee")