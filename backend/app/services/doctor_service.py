# app/services/doctor_service.py
from app.models.user import User
from app.models.doctor import Doctor

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

# get all doctors with department id 
def get_department_doctors(dept_id):
    doctors = Doctor.query.filter_by(department_id = dept_id).all()
    return [
        {
            "id" : d.id,
            "email" : d.user.email
        }
        for d in doctors
    ]