from celery import Celery

app = Celery('crawler', broker='amqp://celery:pw123456@rabbitmq:5672/celery_vhost')
app.config_from_object('crawler.celery_config')
