# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

class DeleteNullTitlePipeline(object):
    def process_item(self, item, spider):
        title = item['title'] 
        if title:
            item['href'] = spider.allowed_domains[0] + item['href']
            return item
        else:
            raise DropItem('found null title %s', item)