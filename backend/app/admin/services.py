from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models import User,Doctor,Patient,Appointment,Department

def dashboard_stats():
    return {
        "total_doctors": Doctor.query.filter_by(is_active=True).count(),
        "total_patients": Patient.query.filter_by(is_active=True).count(),
        "total_appointments": Appointment.query.count()
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
        department_id=department,
        availablity={}
    )
    
    db.session.add(doctor)
    db.session.commit()
    
    return {"message": "Doctor created successfully"}

def search_doctors(query):
    doctors = (
        Doctor.query
        .join(User)
        .filter(
            User.email.ilike(f"%{query}%"),
            Doctor.is_active == True
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
            Patient.is_active == True
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