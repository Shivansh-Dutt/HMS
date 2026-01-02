# app/services/appointment_service.py

from app.models.appointment import Appointment
from app.models.doctor import Doctor
from app.models.patient import Patient
from sqlalchemy.orm import joinedload

def get_all_appointments():
    appointments = (
        Appointment.query
        .options(
            joinedload(Appointment.doctor).joinedload(Doctor.user),
            joinedload(Appointment.doctor).joinedload(Doctor.department),
            joinedload(Appointment.patient).joinedload(Patient.user),
        )
        .all()
    )

    return [
        {
            "id": ap.id,
            "doctor": ap.doctor.user.email,
            "patient": ap.patient.user.email,
            "department": ap.doctor.department.name,
            "is_active": ap.is_active,
        }
        for ap in appointments
    ]

def get_patient_appointments(user_id):
    patient = Patient.query.filter_by(user_id=user_id, is_active=True).first_or_404()
    
    appointments = (
        Appointment.query
        .filter(
            Appointment.patient_id == patient.id,
            # Appointment.date >= date.today()
        )
        .order_by(Appointment.date, Appointment.time)
        .all()
    )
    
    return [
        {
            "appointment_id": a.id,
            "doctor": a.doctor.user.email,
            "date": a.date.isoformat(),
            "time": a.time.strftime("%H:%M"),
            "status": a.status
        }
        for a in appointments
    ]