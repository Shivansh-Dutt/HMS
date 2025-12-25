import csv
from celery_worker import celery
from app.models import Patient, Appointment

@celery.task
def export_patient_history(patient_id):
    patient = Patient.query.get(patient_id)
    
    filename = f"patient_{patient_id}_history.csv"
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date","Status","Diagnosis","Prescription"])
        
        for ap in patient.appointments:
            writer.writerow([
                ap.date,
                ap.status,
                ap.treatment.diagnosis if ap.treatment else "",
                ap.treatment.prescription if ap.treatment else ""
            ])
            
    print(f"CSV export ready: {filename}")
    
# Later
# Store file in DB
# Notify user