from app.extensions import db
from app.models import Appointment
from app.appointments.validators import can_transition

def change_status(appointment, new_status):
    if not can_transition(appointment.status, new_status):
        raise ValueError("Invalid status transition")
    
    appointment.status = new_status
    db.session.commit()