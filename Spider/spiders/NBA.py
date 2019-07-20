"""
Crawl name : NBA
create date : 2019/07/16
Author : Jerry Hsieh
"""


import scrapy
import logging
from scrapy.http import FormRequest
from Spider.FullSpider.items import FullspiderItem
from datetime import datetime

class NBASpider(scrapy.Spider):
	name = 'NBA'
	allowed_domains = ['nba.udn.com']
	start_urls = ('https://nba.udn.com/nba/news/', )

	_retries = 0
	MAX_RETRY = 1

	_pages = 0
	MAX_PAGES = 2

	def parse(self, response):
		for href in response.xpath('//div[@id="news_list_body"]/dl/dt/a/@href').extract():
			url = response.urljoin(href)
			yield scrapy.Request(url, callback=self.parse_post)

		self._pages += 1
		if self._pages < NBASpider.MAX_PAGES:
			next_page = response.xpath('//gonext/a[@data-id="right"]/@href')
			if next_page:
				url = response.urljoin(next_page[0].extract())
				logging.warning('follow {}'.format(url))
				yield scrapy.Request(url, self.parse)
			else:
				logging.warning('no next page')
		else:
			logging.warning('max pages reached')

	def parse_post(self, response):
		article_contant = response.xpath('//div[@id="story_body_content"]/span/p//text()').extract()
		basic_info = response.xpath('//div[@class="shareBar__info--author"]//text()').extract()
		title_info = response.xpath('//h1[@class="story_art_title"]//text()').extract()
		

		item = FullspiderItem()
		item['id'] = response.url.split('/')[-1]
		item['title'] = title_info[0]
		item['datetime'] = basic_info[0]
		item['author'] = basic_info[1]
		item['content'] = ''.join(article_contant)
		item['url'] = response.url
			# return event
		yield item