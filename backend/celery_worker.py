from celery import Celery
from app.config import Config

celery = Celery(
    "hms",
    broker=Config.CELERY_BROKER_URL,
    backend=Config.CELERY_RESULT_BACKEND
)