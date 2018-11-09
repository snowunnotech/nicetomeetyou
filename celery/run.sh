python wait_rabbitmq.py
celery -A celery_app beat -f log/celery_beat.log --detach
celery -A celery_app worker -l info -f log/celery_worker.log
