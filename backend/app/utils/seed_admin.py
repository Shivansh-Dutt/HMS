from app import create_app
from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash

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