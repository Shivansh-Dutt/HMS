from app.extensions import db
from .base import BaseModel

class Doctor(BaseModel):
    __tablename__ = "doctors"
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),nullable=False)
    department_id = db.Column(db.Integer,db.ForeignKey("departments.id"))
    
    specialization = db.Column(db.String(100))
    availablity = db.Column(db.JSON)
    
    # appointments = db.relationship("Appointment", backref="doctor")

    appointments = db.relationship("Appointment", back_populates="doctor")    
    department = db.relationship("Department",back_populates="doctors")