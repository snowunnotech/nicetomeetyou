# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
from udn_news.models import TopNews


class TopNewsBotPipeline(object):
    def process_item(self, item, spider):
        try:
            TopNews.objects.get(title=item['title'])
        except TopNews.DoesNotExist:    
            topNews = TopNews()
            topNews.unique_id = item['unique_id']
            topNews.title = item['title']
            topNews.date = item['date']
            topNews.data = item['data']
            topNews.save()
        return item
