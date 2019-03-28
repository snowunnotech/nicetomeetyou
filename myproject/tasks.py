
from celery import Celery
from myproject.core.crawler import simpleCrawler

app = Celery('tasks', broker='django://')

@app.task
def runCrawler():
    simpleCrawler.run()
    