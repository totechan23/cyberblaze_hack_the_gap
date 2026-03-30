from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import ComplaintDB

router = APIRouter()

@router.post("/create")
def create_complaint(user: str, text: str, location: str, db: Session = Depends(get_db)):

    new_comp = ComplaintDB(
        user=user,
        text=text,
        location=location,
        status="Pending",
        priority="Medium",
        department="General"
    )

    db.add(new_comp)
    db.commit()
    db.refresh(new_comp)

    return {"message": "Complaint stored", "id": new_comp.id}


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    return db.query(ComplaintDB).all()
