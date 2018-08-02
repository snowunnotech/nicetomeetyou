from __future__ import absolute_import, unicode_literals
# from celery import shared_task, task
from scrapy import cmdline, commands, command
# # from celery.task.schedules import crontab
# # from celery.decorators import periodic_task
# import time
#
# # @periodic_task(run_every=crontab())
# @task
# def runspider():
#     cmdline.execute('scrapy crawl nba'.split())

from celery import shared_task
from scrapy.utils.log import configure_logging


@shared_task
def runspider():
    # configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    cmdline.execute('scrapy crawl nba'.split())