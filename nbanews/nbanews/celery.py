from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nbanews.settings')

app = Celery('nbanews')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
#app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
#app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERYBEAT_SCHEDULE = {
        #every one minute exceute
        'nba_news_grab': {
            'task': 'news.tasks.news_grab',
            'schedule':  timedelta(minutes=1),
            'args': ()
        },
    }
)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))