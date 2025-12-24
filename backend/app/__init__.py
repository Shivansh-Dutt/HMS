from flask import Flask
from .config import Config
from .extensions import db, jwt, cache
from app.auth.routes import auth_bp
from app.admin.routes import admin_bp
from app.doctor.routes import doctor_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    cache.init_app(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(doctor_bp)
    
    @app.route("/health")
    def health():
        return {"status": "ok"}
    
    return app
