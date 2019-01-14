""" Create a superuser
"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'nba_news_backend.settings'
import django
django.setup()
from django.contrib.auth.models import User

if User.objects.filter(username=os.environ['DJANGO_ADMIN_ACCOUNT']):
    print('Super user already exists. SKIPPING...')
else:
    User.objects.create_superuser(
        os.environ['DJANGO_ADMIN_ACCOUNT'],
        os.environ['DJANGO_ADMIN_EMAIL'],
        os.environ['DJANGO_ADMIN_PASSWORD']
    )
    print('Super user created...')
