# app/services/patient_service.py
from app.models.user import User

def get_all_patients():
    patients = User.query.filter_by(role="PATIENT").all()
    return [
        {
            "id": p.id,
            "email": p.email,
            "is_active": p.is_active
        }
        for p in patients
    ]
