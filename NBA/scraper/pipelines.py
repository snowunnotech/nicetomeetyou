# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from news.models import NBANews

class ScraperPipeline(object):
    def process_item(self, item, spider):
  
        if NBANews.objects.filter(title = item['title']):
            print('news repeat')
            return None
        else:
            item.save()
            return item
