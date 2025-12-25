import os 
from celery.schedules import crontab

class Config:
    """Base configuration class."""
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    SQLALCHEMY_DATABASE_URI = "sqlite:///hms_v2.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = "jwt-secret"
    
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
    
    beat_schedule = {
    "daily-reminders": {
        "task": "app.tasks.reminders.send_daily_reminders",
        "schedule": crontab(hour=8, minute=0),
    },
    "monthly-reports": {
        "task": "app.tasks.reports.generate_monthly_reports",
        "schedule": crontab(day_of_month=1, hour=2),
    },
}