from celery.task import periodic_task
from News.models import Article
from News.crawler import getNews
from datetime import timedelta

# 加了這個裝飾器後等同於註冊該函式為task
@periodic_task(run_every=timedelta(seconds=5))
def task_get_news():
    try:
        for news in getNews():
            if not Article.objects.filter(title=news['title']).exists():
                article = Article(title=news['title'], 
                                img_url=news['image_url'], 
                                url=news['url'], 
                                content=news['content'])
                article.save()

    except Exception as e:
        print (e)