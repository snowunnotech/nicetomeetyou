# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from crawler.models import NBAnews

class ScraperPipeline(object):
    def process_item(self, item, spider):
        title = item['title'][0]
        if NBAnews.objects.filter(title = title):
            return None
        content = ''.join(item['content'][4:])
        item['content'] = content
        item['title'] = title
        item.save()
        return item
