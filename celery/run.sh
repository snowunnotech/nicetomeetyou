python wait_rabbitmq.py
celery -A celery_app worker -B -l info -f log/celery_worker.log
