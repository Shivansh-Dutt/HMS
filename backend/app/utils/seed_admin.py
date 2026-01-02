from app import create_app
from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash
from app.models import Department , Appointment
import datetime

app = create_app()

with app.app_context():
    if not User.query.filter_by(role="ADMIN").first():
        admin = User(
            email="admin@hms.com",
            password=generate_password_hash("admin123"),
            role="ADMIN"
        )
        db.session.add(admin)
        db.session.commit()
        print("Admin created")
        
    print("Seeding Database...")
    # ---- Departments ----
    # departments = [
    #     Department(name="Cardiology", description="Heart specialists"),
    #     Department(name="Neurology", description="Brain & nervous system"),
    #     Department(name="Orthopedics", description="Bones and joints"),
    #     Department(name="Pediatrics", description="Child specialists"),
    # ]
    # db.session.add_all(departments)
    # db.session.commit()
    # print("✅ Departments added")
     
    #--- Appointments ---
    # appointments = [
    #     Appointment(doctor_id=2,patient_id=1,date=datetime.datetime.now().date(),time=datetime.datetime.now().time())
    # ]
    # db.session.add_all(appointments)
    # db.session.commit()
    # print("Appointment Booked")