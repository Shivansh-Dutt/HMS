from app.models import Appointment

def can_transition(current_status,new_status):
    allowed = {
        "BOOKED": {"COMPLETED", "CANCELLED"},
        "COMPLETED": set(),
        "CANCELLED": set()
    }
    return new_status in allowed[current_status]

def is_slot_available(doctor_id, date, time):
    return not Appointment.query.filter_by(
        doctor_id=doctor_id,
        date=date,
        time=time,
        status="BOOKED"
    ).first()