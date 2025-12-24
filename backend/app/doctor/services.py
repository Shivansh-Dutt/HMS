from datetime import date
from app.models import Doctor, Appointment , Patient ,Treatment
from app.extensions import db

def get_upcoming_appointments(user_id):
    doctor = Doctor.query.filter_by(user_id=user_id, is_active=True).first_or_404()
    
    appointments = (
        Appointment.query
        .filter(
            Appointment.doctor_id == doctor.id,
            Appointment.date >= date.today(),
            Appointment.status == "BOOKED"
        )
        .order_by(Appointment.date, Appointment.time)
        .all()
    )
    
    return [
        {
            "appointment_id": a.id,
            "data" : a.date.isoformat(),
            "time" : a.time.strftime("%H:%M"),
            "patient_id" : a.patient.id,
            "patient_email" : a.patient.user.email
        }
        for a in appointments
    ]
    
def get_assigned_patients(user_id):
    doctor = Doctor.query.filter_by(user_id=user_id).first_or_404()
    
    patients = {
        ap.patient for ap in doctor.appointments if ap.patient.is_active
    }
    
    return [
        {
            "patient_id": p.id,
            "email": p.user.email,
            "contact": p.contact
        }
        for p in patients
    ]
    
def update_appointment_status(user_id, appointment_id):
    doctor = Doctor.query.filter_by(user_id=user_id).first_or_404()
    
    appointment = Appointment.query.filter_by(
        id=appointment_id,
        doctor_id=doctor.id
    ).first_or_404
    
    appointment.status = "COMPLETED"
    db.session.commit()
    
    return {"message": "Appointment marked as completed"}

def create_treatment(user_id, appointment_id, data):
    doctor = Doctor.query.filter_by(user_id==user_id).first_or_404()
    
    appointment = Appointment.query.filter_by(
        id=appointment_id,
        doctor_id=doctor.id,
        status="COMPLETED"
    ).first_or_404
    
    if appointment.treatment:
        raise ValueError("Treatment already exists")
    
    treatment = Treatment(
        appointment_id=appointment.id,
        diagnosis=data.get("diagnosis"),
        prescription=data.get("prescription"),
        notes=data.get("notes")
    )

    db.session.add(treatment)
    db.session.commit()

    return {"message": "Treatment record added"}

def get_patient_history(user_id,patient_id):
    doctor = Doctor.query.filter_by(user_id=user_id).first_or_404()
    
    appointments = (
        Appointment.query
        .filter(
            Appointment.patient_id == patient_id,
            Appointment.doctor_id == doctor.id
        )
        .all()
    )
    
    return [
        {
            "date": a.status.isoformat(),
            "status": a.status,
            "diagnosis": a.treatment.diagnosis if a.treatment else None,
            "prescription": a.treatment.prescription if a.treatment else None
        }
        for a in appointments
    ]
    
def update_doctor_availablity(user_id,availablity):
    doctor = Doctor.query.filter_by(user_id=user_id).first_or_404
    
    doctor.availablity = availablity
    db.session.commit()
    
    return {"message": "Availablity updated"}