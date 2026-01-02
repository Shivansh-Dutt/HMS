from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models import User,Doctor,Patient,Department
from app.services.patient_service import get_all_patients
from app.services.doctor_service import get_all_doctors
from app.services.appointment_service import get_all_appointments

def get_admin_dashboard():
    return {
        "total_doctors": get_all_doctors(),
        "total_patients": get_all_patients(),
        "upcoming_appointments": get_all_appointments()
    }
    
def create_doctor(data):
    dept_id = data.get("department_id")
    
    department = Department.query.get(dept_id)
    if not department:
        return {"error": "Department not found"}, 400
    
    user = User(
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role="DOCTOR"
    )
    db.session.add(user)
    db.session.flush()

    doctor = Doctor(
        user_id = user.id,
        specialization=data.get("specialization"),
        department_id=department.id,
        availablity={}
    )
    
    db.session.add(doctor)
    db.session.commit()
    
    return {"message": "Doctor created successfully"} , 201

def search_doctors(query):
    doctors = (
        Doctor.query
        .join(User)
        .filter(
            User.email.ilike(f"%{query}%"),
            Doctor.is_active
        )
        .all()
    )
    
    return [
        {
            "id": d.id,
            "email": d.user.email,
            "specializaton": d.specialization
        }
        for d in doctors
    ]
    
def search_patients(query):
    patients = (
        Patient.query
        .join(User)
        .filter(
            User.email.ilike(f"%{query}%"),
            Patient.is_active
        )
        .all()
    )
    
    return [
        {
            "id": p.id,
            "email" : p.user.email,
            "contact" : p.contact
        }
        for p in patients
    ]
    
def disable_user(user_id):
    user = User.query.get_or_404(user_id)
    user.is_active = False
    db.session.commit()
    
    return {"message": "User disabled successfully"}