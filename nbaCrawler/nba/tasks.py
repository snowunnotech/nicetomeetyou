from celery.task import task
from nba.models import News
from nba.crawler import crawler

@task()
def getNews():
    for news in crawler.getNews():
        if(not News.objects.filter(title=news['title']).exists()):
            n = News(title=news['title'], url=news['url'], content=news['content'])
            n.save()