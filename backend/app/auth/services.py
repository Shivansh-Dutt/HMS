from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from app.models import User

def login_user(email, password):
    user = User.query.filter_by(email=email, is_active=True).first()
    
    if not user:
        raise ValueError("Invalid credentials")
    
    if not check_password_hash(user.password, password):
        raise ValueError("InValid Credentials")
    
    token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role}
    )
    
    return {
        "access_token": token,
        "role": user.role,
        "email": user.email
    }