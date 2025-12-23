from flask import Flask
from .config import Config
from .extensions import db, jwt, cache
from app.auth.routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    cache.init_app(app)
    
    app.register_blueprint(auth_bp)
    
    @app.route("/health")
    def health():
        return {"status": "ok"}
    
    return app
