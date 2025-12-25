from celery import Celery
from app import create_app
from app.config import Config

def make_celery():
    app = create_app()
    
    celery = Celery(
        app.import_name,
        broker=Config.CELERY_BROKER_URL,
        backend=Config.CELERY_RESULT_BACKEND
    )
    
    celery.conf.update(app.config)
    
    class ContextTask(celery.Task):
        def __call__(self,*args,**kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
            
    celery.Task = ContextTask
    return celery

celery = make_celery()