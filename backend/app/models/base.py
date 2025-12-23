from app.extensions import db 

class BaseModel(db.Model):
    # tells SQLAlchemy not to create a database table for BaseModel.
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    is_active = db.Column(db.Boolean, default=True)