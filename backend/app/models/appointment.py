from app.extensions import db
from .base import BaseModel

class Appointment(BaseModel):
    __tablename__ = "appointments"
    
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)

    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Date, nullable=False)
    
    status = db.Column(db.String(20), default="BOOKED")
    
    # treatment = db.relationship("Treatment", backref="appointment", uselist=False)
    
    doctor = db.relationship("Doctor", back_populates="appointments")
    patient = db.relationship("Patient",back_populates="appointments")
    
    treatment = db.relationship("Treatment", back_populates="appointment",uselist=False)
    
    __table_args__ = (
        db.UniqueConstraint(
            "doctor_id", "date", "time",
            name="unique_doctor_slot"
        ),
    )