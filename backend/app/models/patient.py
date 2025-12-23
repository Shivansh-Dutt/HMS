from app.extensions import db
from .base import BaseModel

class Patient(BaseModel):
    __tablename__ = "patients"
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    age = db.Column(db.Integer)
    contact = db.Column(db.String(20))
    address = db.Column(db.Text)
    
    # appointments = db.relationship("Appointment",backref="patient")
    
    appointments = db.relationship("Appointment",back_populates="patient")
    user = db.relationship("User",back_populates="patient",uselist=False)