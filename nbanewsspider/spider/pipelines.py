# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from spider.postgres_provider import PostgresProvider
from spider.settings import DATABASES

class SpiderPipeline(object):
    def open_spider(self, spider):
        self.postgres_provider = PostgresProvider()
        self.postgres_provider.connect(
            DATABASES['default']['USER'],
            DATABASES['default']['PASSWORD'],
            DATABASES['default']['NAME'],
            DATABASES['default']['HOST'])
        self.connection = self.postgres_provider.connection
        self.meta = self.postgres_provider.meta

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        news = self.meta.tables['nbanewsreader_news']
        clause = news.insert().values(
            uid=item['uid'],
            url=item['url'],
            title=item['title'],
            author=item['author'],
            published_at=item['published_at'],
            content=item['content'])
        self.connection.execute(clause)
        return item
