
from celery import Celery
from myproject.core.crawler import SimpleCrawler

app = Celery('tasks', broker='django://')

@app.task
def runCrawler():
    SimpleCrawler.run()
    