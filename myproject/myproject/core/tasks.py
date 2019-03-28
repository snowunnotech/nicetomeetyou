
import celery
from myproject.core.crawler import SimpleCrawler

@celery.task()
def run_crawler():
    SimpleCrawler.run()
