celery -A celery_app beat
celery -A celery_app worker -l info
