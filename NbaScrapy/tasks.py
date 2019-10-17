from __future__ import absolute_import, unicode_literals
from scrapy import cmdline
from celery import shared_task
import os

@shared_task
def InitRun():
    os.system('scrapy crawl NBA')