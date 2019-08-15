from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery(
    'mysite',
    broker=os.getenv('broker',''),
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'premium-check-and-charge': {
            'task': 'payment.tasks.premium_check',
            # UTC 16:00 == UTC+8 0:00 == 當天午夜檢查是否過期
            'schedule': crontab(minute=0, hour=16),
            # 'schedule': timedelta(seconds=60),
        },
        # 'test': {
        #     'task': 'deploy.tasks.add',
        #     'schedule': timedelta(seconds=5),
        # }
    }
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))