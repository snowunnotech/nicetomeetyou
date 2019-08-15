from celery import shared_task
from celery.task.schedules import crontab  
from celery.decorators import periodic_task

from .services import *
import json, requests, os
from helper.helper import APIHandler
import logging

# Get an instance of a logger
logger = logging.getLogger('django.request')

@shared_task
def NBA_Crawl():
    url = os.getenv('NBA_URL')
    zip_data = CRAW(url)
    new_news_ids = []
    for data in zip_data:
        news_state = CHECK_EXIST(data)
        if news_state:
            continue
        else:
            news_id = SAVE_NEWS(data)
            new_news_ids.append(news_id)
    if new_news_ids:
        logger.info('Sccessfully got new news')
        return APIHandler.catch(data={'news_ids':new_news_ids}, code='001')
    else:
        logger.info('Nothing new')
        return APIHandler.catch(data='Nothing new', code='000')