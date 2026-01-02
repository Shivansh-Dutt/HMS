# app/services/doctor_service.py
from app.models.user import User

def get_all_doctors():
    doctors = User.query.filter_by(role="DOCTOR").all()
    return [
        {
            "id": p.id,
            "email": p.email,
            "is_active": p.is_active
        }
        for p in doctors
    ]
