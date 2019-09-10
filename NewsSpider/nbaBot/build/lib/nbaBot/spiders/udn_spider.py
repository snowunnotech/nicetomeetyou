import scrapy
from nbaBot.items import NbabotItem
from datetime import datetime

class UdnSpider(scrapy.Spider):
	name = "udn_spider"
	allowed_domains = ['nba.udn.com']
	start_urls = [
		'https://nba.udn.com/nba/index?gr=www',
	]

	def parse(self, response):
		news_body = response.css('div[id="news_body"]')
		for news in news_body.css('dt'):
			href = news.css('a::attr(href)')
			if len(href) > 0:
				news_url = response.urljoin(href.extract_first())
				yield scrapy.Request(news_url, callback = self.parseNewsPage)

	def parseNewsPage(self, response):
		sb = response.css('div[id="story_body"]')
		nid = sb.css('::attr(data-sub)').extract_first() + '_' +  sb.css('::attr(data-article)').extract_first()

		story = response.css('div[id="story_body_content"]')
		title = story.css('h1.story_art_title::text').extract_first()
		date = story.css('div.shareBar__info--author span::text').extract_first()
		author = story.css('div.shareBar__info--author::text').extract_first()

		article = ""
		article_content = story.css('span')
		for paragraph in article_content.css('p'):
			if len(paragraph.css('figure')) > 0:
				# todo get image
				continue

			tmpText = ''
			for pt in paragraph.css('::text'):
				tmpText += pt.extract()
			
			if tmpText != '':
				article += tmpText + '\n'

		item = NbabotItem()
		item['news_id'] = nid
		item['title'] = title
		item['date'] = datetime.strptime( date, "%Y-%m-%d %H:%M")
		item['author'] = author
		item['content'] = article
		yield item