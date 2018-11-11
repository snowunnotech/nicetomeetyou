from datetime import timedelta
from celery.schedules import crontab

# Timezone
timezone = 'Asia/Taipei'

# import
imports = (
    'celery_app.tasks',
)

# result
result_backend = 'db+sqlite:///db.sqlite3'

# schedules
beat_schedule = {
    'every-5-minutes': {
        'task': 'celery_app.tasks.chain_crawler',
        'schedule': timedelta(minutes=1),
    }
}
