from scrapyd_api import ScrapydAPI
from celery import shared_task
from django.conf import settings
# connect scrapyd service
scrapyd = ScrapydAPI(settings.SCRAPYD_URL)

@shared_task()
def activate_spider():
    try:
        scrapyd.schedule('crawler_app', 'nba')
    except ConnectionError:
        print('Cannot connect scrapyd.')
