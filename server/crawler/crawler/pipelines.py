# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from api.models import HotNews


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        # if len(HotNews.objects.filter(image_url=item['image_url'], title=item['title'])) == 0:
        #     item.save()
        # else:
        #     spider.close_down = True
        #     # spider.crawler.engine.close_spider(self, reason='finished')

        # 這樣一個一個存484沒效率阿
        item.save()
        return item
