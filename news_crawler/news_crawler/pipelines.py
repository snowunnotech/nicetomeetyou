# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from news.models import Articles

class NewsCrawlerPipeline(object):
    def process_item(self, item, spider):
        try:
            article = Articles.objects.get(title=item['title'])
            print('article exists.')
            return item
        except Articles.DoesNotExist:
            pass

        article = Articles()
        article.title = item['title']
        article.pub_time = item['pub_time']
        article.content = item['content']
        article.save()

        return item
