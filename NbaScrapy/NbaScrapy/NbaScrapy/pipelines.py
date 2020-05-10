# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from NBAframework.models import NBAframework

class NbascrapyPipeline(object):
    def process_item(self, item):
        try:
            nbanews = NBAframework.objects.get(title=item['title'])
            print('News already exist')
            return item
        except NBAframework.DoesNotExist:
            # print('News does not exist')
            pass

        nbanews = NBAframework()
        nbanews.title = item['title']
        nbanews.publish_date = item['publish_date']
        nbanews.author = item['author']
        nbanews.image_url = item['image_url']
        nbanews.image_caption = item['image_caption']
        nbanews.video_url = item['video_url']
        nbanews.content = item['content']
        nbanews.save()

        return item

    def spider_closed(self, spider):
        return True
