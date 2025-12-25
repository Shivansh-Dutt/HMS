from datetime import date
from celery_worker import celery
from app.models import Doctor, Appointment

@celery.task
def generate_monthly_reports():
    doctors = Doctor.query.filter_by(is_active=True).all()
    
    for doctor in doctors:
        appointments = Appointment.query.filter(
            Appointment.doctor_id == doctor.id
        ).all()
        
        print(
            f"Monthly report for Dr.{doctor.user.email}"
            f"{len(appointments)} appointments"
        )
        
# Later
# Generate HTML
# Convert to PDF
# Email it