from datetime import timedelta
from celery.schedules import crontab

# Timezone
timezone = 'Asia/Taipei'

# import
imports = (
    'crawler.tasks',
)

# result
result_backend = 'db+sqlite:///db.sqlite3'

# schedules
beat_schedule = {
    'every-5-minutes': {
        'task': 'news.tasks.add',
        'schedule': timedelta(minutes=5),
    }
}