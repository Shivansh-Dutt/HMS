from app.extensions import db
from .base import BaseModel

class Department(BaseModel):
    __tablename__ = "departments"
    
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    
    doctors = db.relationship("Doctor",back_populates="department")