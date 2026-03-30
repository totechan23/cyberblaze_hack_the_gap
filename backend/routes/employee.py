# backend/routes/employee.py

from fastapi import APIRouter
from routes.complaint import complaints_db

router = APIRouter()

@router.get("/dashboard")
def employee_dashboard():
    return {
        "total_complaints": len(complaints_db),
        "complaints": complaints_db
    }

@router.put("/update-status/{complaint_id}")
def update_status(complaint_id: str, status: str):
    for comp in complaints_db:
        if comp["id"] == complaint_id:
            comp["status"] = status
            return {"message": "Status updated"}
    
    return {"error": "Complaint not found"}
