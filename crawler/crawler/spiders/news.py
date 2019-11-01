import os
import scrapy
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
		rawimgurl = response.xpath('//div[@id="story_body_content"]/span//a/img/@data-src').get()
		item['image_urls'] = [rawimgurl.split('u=')[1].split('&')[0], ]

		yield item