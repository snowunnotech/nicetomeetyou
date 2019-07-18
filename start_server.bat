DEL celerybeat-schedule.dir
DEL celerybeat.pid
DEL celerybeat-schedule.bak
DEL celerybeat-schedule.dat
START Redis\redis-server.exe
START python manage.py runserver
START celery -A webdata beat -l info
START celery -A webdata worker -l info
TIMEOUT /t 5
EXPLORER "http://127.0.0.1:8000/index"