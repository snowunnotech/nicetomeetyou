# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from datetime import datetime


class FullspiderPipeline(object):

	def open_spider(self, spider):
		db_name = spider.settings.get('MySpider', 'scrapy.db')
		self.db_conn = sqlite3.connect(db_name)
		self.db_cur = self.db_conn.cursor()

	def process_item(self, item, spider):
		self.insert_db(item)
		return item

	def close_spider(self, spider):
		self.db_conn.commit()
		self.db_conn.close()

	def insert_db(self, item):
		values = (
			int(item.get('id','')),
			item.get('title',''),
			item.get('author',''),
			item.get('datetime',''),
			item.get('content',''),
			item.get('url','')
		)

		sql = """INSERT INTO cr_nba (`id`,`title`,`author`,`datetime`,`content`,`url`)
		VALUES
		(?,?,?,?,?,?)"""
		self.db_cur.execute(sql, values)
		
	# def from_crawler <- default