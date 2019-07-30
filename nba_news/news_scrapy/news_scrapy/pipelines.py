# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NewsScrapyPipeline(object):
    def process_item(self, item, spider):
        item['title'] = item['title'][0]
        # item['url'] = item['url']
        item['content'] = ''.join(item['content'])
        item['figure_url'] = item['figure_url'][0]
        # item['crawled_time'] = item['crawled_time']
        item['published_time'] = item['published_time'][0]
        item.save()
        return item
    