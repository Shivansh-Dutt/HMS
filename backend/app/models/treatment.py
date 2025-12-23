from app.extensions import db
from .base import BaseModel

class Treatment(BaseModel):
    __tablename__ = "treatments"
    
    appointment_id = db.Column(
        db.Integer,
        db.ForeignKey("appointments.id"),
        nullable=False,
        unique=True
    )
    
    diagnosis = db.Column(db.Text)
    prescription = db.Column(db.Text)
    notes = db.Column(db.Text)
    
    appointment = db.relationship("Appointment", back_populates="treatment", uselist=False)