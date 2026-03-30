# backend/database/models.py

from sqlalchemy import Column, String
from database.db import Base
import uuid

# -------------------
# USER TABLE
# -------------------
class UserDB(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)  # citizen / employee


# -------------------
# COMPLAINT TABLE
# -------------------
class ComplaintDB(Base):
    __tablename__ = "complaints"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user = Column(String)
    text = Column(String)
    location = Column(String)

    status = Column(String, default="Pending")
    priority = Column(String, default="Medium")
    department = Column(String)


# -------------------
# SOS TABLE
# -------------------
class SOSDB(Base):
    __tablename__ = "sos"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user = Column(String)
    location = Column(String)
    message = Column(String)