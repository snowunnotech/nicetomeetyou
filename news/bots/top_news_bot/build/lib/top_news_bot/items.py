import scrapy
from django.db import models
from django.utils import timezone
# from udn_news.models import TopNews


class TopNewsBotItem(scrapy.Item):
    unique_id = scrapy.item.Field()
    title = scrapy.item.Field()
    date = scrapy.item.Field()
    data = scrapy.item.Field()
    # django_model = TopNews
    # title = models.TextField()
    # date = models.DateTimeField(default=timezone.now)
    # data = models.TextField()

    # class Meta:
    #     app_label = 'news'
    #     db_table = 'top_news_spider'
    def __str__(self):
        return self.unique_id
