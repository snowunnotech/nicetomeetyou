# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from main.models import NewsModel

class ScrapyAppPipeline(object):
    def process_item(self, item, spider):
        news = NewsModel(title = item['title'], 
                         link_url = item['link_url'], 
                         img_url = item['img_url'])
        news.save()
        return item
