from celery_worker import celery
from datetime import date
from app.models import Appointment

@celery.task
def send_daily_reminders():
    appointments = Appointment.query.filter_by(
        date=date.today(),
        status="BOOKED"
    ).all()
    
    for ap in appointments:
        print(
            f"Reminder: Appointment for "
            f"{ap.patient.user.email}"
            f"with Dr. {ap.doctor.user.email}" 
        )

# Later change to email/SMS