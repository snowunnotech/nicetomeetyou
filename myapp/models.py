from django.db import models
from .crawler import get_current_news
from datetime import datetime,timedelta


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_time = models.DateTimeField()
    source = models.CharField(max_length=255)

    @classmethod
    def from_json(cls, json_dict):
        instance = cls()
        for key, value in json_dict.items():
            setattr(instance, key, value)
        return instance

    def __str__(self):
        return f"標題：{self.title}\n時間：{self.post_time}\n{self.content}來源：{self.source}"


class Latest(models.Model):
    latest_news = models.ForeignKey(News, on_delete=models.CASCADE)


def update_news(latest_time):
    all_news = get_current_news()
    all_news = [News.from_json(news_dict) for news_dict in all_news if news_dict["post_time"] - latest_time > timedelta(minutes=5)]
    if not all_news:
        return
    latest_news = max(all_news, key=lambda n: n.post_time)
    latest = Latest()
    for news in all_news:
        news.save()
    print(f"{len(all_news)} news updated")
    latest.latest_news = latest_news
    latest.save()


try:
    if not News.objects.all():
        update_news(datetime(year=1970,month=1,day=1))
except Exception as e:
    print(e)
