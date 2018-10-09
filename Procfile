release: python manage.py migrate
web: gunicorn newsfeed.wsgi --log-file -
beat: python manage.py qcluster