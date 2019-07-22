# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
import logging

INSERT_SQL = "INSERT INTO news_nba (title, date_time, author, content, image_source, video_source, article_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"

class CrawlerPipeline(object):
    def __init__(self, db_url):
        self.conn = psycopg2.connect(db_url)
        self.cur = self.conn.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_url = crawler.settings.get('DATABASE_URL')
        )
        
    def process_item(self, item, spider):
        try:
            self.cur.execute(INSERT_SQL, (item.get('title'), item.get('date_time'), item.get('author'), item.get('content'), item.get('image_source'), item.get('video_source'), item.get('article_url')))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logging.error(str(e))
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
