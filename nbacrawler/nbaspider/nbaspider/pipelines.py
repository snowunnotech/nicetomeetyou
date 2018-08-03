# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from nbanews.models import NBANewsModel


class NbaspiderPipeline(object):
    def process_item(self, item, spider):
        try:
            nbanews = NBANewsModel.objects.get(title=item['title'])
            print('News already exist')
            return item
        except NBANewsModel.DoesNotExist:
            # print('News does not exist')
            pass

        nbanews = NBANewsModel()
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
