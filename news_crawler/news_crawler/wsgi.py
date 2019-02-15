import sys
"""
WSGI config for news_crawler project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

sys.path.append(
    '/opt/bitnami/apps/django/django_projects/nicetomeetyou/news_crawler')
os.environ.setdefault(
    "PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/nicetomeetyou/news_crawler/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_crawler.settings")

application = get_wsgi_application()
