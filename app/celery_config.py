from celery import Celery

celery = Celery(
    'app',
    # broker='redis://localhost:6379/0',
    broker='redis://default:Ygcj1FxTyYPXlkpImP4zxw1QTNiHBvkH@redis-11437.c277.us-east-1-3.ec2.cloud.redislabs.com:11437',
    # backend='redis://localhost:6379/0',
    backend='redis://default:Ygcj1FxTyYPXlkpImP4zxw1QTNiHBvkH@redis-11437.c277.us-east-1-3.ec2.cloud.redislabs.com:11437',
)

celery.conf.update(
    result_expires=3600,
)
