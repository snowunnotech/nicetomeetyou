import os
import scrapy
import sqlite3
from crawler.items import NewsItem


class NewsSpider(scrapy.Spider):
	name = 'nba'
	allowed_domains = ['nba.udn.com']
	start_urls = ['https://nba.udn.com/nba/index?gr=www']

	def parse(self, response):

		res = response.xpath('//div[@id="news_body"]/dl/dt/a/@href').getall()

		for newsblock in res:
			yield scrapy.Request('https://nba.udn.com'+newsblock, callback=self.newspage, encoding='utf-8')

	def newspage(self, response):
		item = NewsItem()
		item['title'] = response.xpath('//div[@id="story_body_content"]/h1/text()').get()
		item['date'] = response.css('div.shareBar__info--author').xpath('./span/text()').get()
		item['author'] = response.css('div.shareBar__info--author::text').get()
		item['content'] = response.xpath('//div[@id="story_body_content"]//p/text()').getall()
		item['content'] = ''.join(item['content'])

		BASE_DIR = os.path.dirname(os.path.abspath('.'))
		conn = sqlite3.connect(BASE_DIR+'\\db.sqlite3')
		c = conn.cursor()
		if not c.execute("select title from SpotNews where title = '" + item['title'] + "'").fetchall():
			sql = "insert into SpotNews (title, date, author, content)"
			sql += str.format(' values ("{0}","{1}","{2}","{3}")', item['title'], item['date'], item['author'], item['content'])
			c.execute(sql)
		conn.commit()
		conn.close()

		yield item