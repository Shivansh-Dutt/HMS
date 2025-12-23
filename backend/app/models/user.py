from app.extensions import db
from .base import BaseModel

class User(BaseModel):
    __tablename__ = "users"
    
    email = db.Column(db.String(120), unique=True,nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    
    doctor = db.relationship("Doctor",backref="user", uselist=False)
    patient = db.relationship("Patient", backref="user", uselist=False)