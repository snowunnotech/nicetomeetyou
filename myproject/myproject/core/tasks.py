
import celery
from myproject.core.crawler import simpleCrawler

@celery.task()
def run_crawler():
    simpleCrawler.run()
