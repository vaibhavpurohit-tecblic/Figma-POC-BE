from celery import Celery

celery = Celery(
    'app',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)

celery.conf.update(
    result_expires=3600,
)
