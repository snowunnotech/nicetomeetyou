# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3

class CrawlerPipeline(object):
	def process_item(self, item, spider):
		BASE_DIR = os.path.dirname(os.path.abspath('.'))
		conn = sqlite3.connect(BASE_DIR+'\\db.sqlite3')
		c = conn.cursor()
		if not c.execute("select title from SpotNews where title = '" + item['title'] + "'").fetchall():
			sql = "insert into SpotNews (title, date, author, content, newsimg)"
			sql += str.format(' values ("{0}","{1}","{2}","{3}","{4}")', item['title'], item['date'],\
							 item['author'], item['content'], item['images'][0]['path'])
			c.execute(sql)
		conn.commit()
		conn.close()
		return item
