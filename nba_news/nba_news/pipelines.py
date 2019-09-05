# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class NbaNewsPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect('/Users/fish/Documents/workspace/nicetomeetyou/NBA_news.db')
        self.cur = self.conn.cursor()
        self.cur.execute('create table if not exists nba_news(id, title, url, date, source, content)')
        # pass

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()
        # pass

    def process_item(self, item, spider):
        col = ','.join(item.keys())
        placeholders = ','.join(len(item) * '?')
        sql = 'insert into nba_news({}) values({})'
        self.cur.execute(sql.format(col, placeholders), item.values())
        return item
