from werkzeug.security import generate_password_hash
# from datetime import date
from app.extensions import db
from app.models import User, Patient, Appointment, Doctor
from sqlalchemy.exc import IntegrityError
from app.tasks.exports import export_patient_history
from app.appointments.services import change_status
from app.appointments.validators import is_slot_available
from app.services.appointment_service import get_patient_appointments
from app.services.department_service import get_all_departments

def register_patient(data):
    if User.query.filter_by(email=data["email"]).first():
        return {"error": "Email already exists"}, 400
    
    user = User(
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role="PATIENT"
    )
    db.session.add(user)
    db.session.flush()
    
    patient = Patient(
        user_id = user.id,
        age=data.get("age"),
        contact=data.get("contact"),
        address=data.get('address')
    )
    
    db.session.add(patient)
    db.session.commit()
    
    return {"message": "Patient registered successfully"}, 201

def get_patient_dashboard(user_id):
    return {
        "upcoming_patient_appointments" : get_patient_appointments(user_id),
        "all_departments"  : get_all_departments()
    }
    
def search_available_doctors(query):
    doctors = (
        Doctor.query
        .join(User)
        .filter(
            Doctor.is_active,
            User.email.ilike(f"%{query}%")
        )
        .all()
    )
    
    return [
        {
            "doctor_id": d.id,
            "email": d.user.email,
            "specialization": d.specialization,
            "availablity": d.availablity
        }
        for d in doctors
    ]
    
def book_appointment(user_id,data):
    patient = Patient.query.filter_by(user_id=user_id).first_or_404()
    
    if not is_slot_available(data["doctor_id"], data["date"], data["time"]):
        raise ValueError("Slot already booked")

    appointment = Appointment(
        doctor_id=data["doctor_id"],
        patient_id=patient.id,
        date=data["date"],
        time=data["time"]
    )
    
    db.session.add(appointment)
    
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise ValueError("Time slot already booked")
    
    return {"message": "Appointment booked successfully"}

def cancel_appointment(user_id, appointment_id):
    patient = Patient.query.filter_by(user_id=user_id).first_or_404()
    appointment = Appointment.query.filter(
        id = appointment_id,
        patient_id = patient.id,
        status = "BOOKED"
    ).first_or_404()
    
    # appointment.status= "CANCELLED"
    change_status(appointment, "CANCELLED")
    db.session.commit()
    
    return {"message": "Appointment cancelled"}

def get_patient_history(user_id):
    patient = Patient.query.filter_by(user_id=user_id).first_or_404()
    
    appointments = Appointment.query.filter_by(
        patient_id = patient.id,
    ).order_by(Appointment.date.desc()).all()
    
    return [
        {
            "date": a.date.isoformat(),
            "status": a.status,
            "diagnosis": a.treatment.diagnosis if a.treatment else None,
            "prescription": a.treatment.prescription if a.treatment else None
        }
        for a in appointments
    ]
    
def export_history_of_patient(user_id):
    patient = Patient.query.filter_by(user_id=user_id).first_or_404()
    
    export_patient_history.delay(patient.id)
    
    return {"message": "Export started. You will be notified"}