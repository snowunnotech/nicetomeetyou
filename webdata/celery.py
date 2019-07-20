import os 
from datetime import datetime , timedelta

from celery import Celery 
from celery.decorators import periodic_task
from celery.task.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdata.settings') 
app = Celery('webdata', broker='redis://localhost:6379/')

@periodic_task(run_every=timedelta(minutes=30))
def some_task():
	from Spider.spiders.NBA import NBASpider
	from tools.scrapy_run import run_scrapy
	run_scrapy(NBASpider)
	print('finished')
