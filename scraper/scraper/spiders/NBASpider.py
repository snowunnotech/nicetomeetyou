import scrapy
from scrapy.spiders import CrawlSpider
from scraper.items import NewItem

class NBASPider(CrawlSpider):
	name = "news"
	start_urls = [
		'https://nba.udn.com/nba/news/',
	]

	def parse(self, response):
		for new in response.css('div#news_list_body dl dt'):
			#yield {
			title =  new.xpath('a/h3/text()').extract_first()
			outline = new.xpath('a/p/text()').extract_first()
			href = ''.join(["https://nba.udn.com",new.css('a::attr("href")').extract_first()])

			item = NewItem()
			item['title'] = title
			item['outline'] = outline
			item['href'] = href
			
			
			yield scrapy.Request(href, callback=self.parse_content, meta={'item': item})

			#yield item
			#}
		
		
		next_page = response.css('div.pagelink gonext a[data-id="right"]::attr("href")').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)
		
	
	def parse_content(self, response):
		# title = response.xpath('//div[@id="story_body_content"]/h1[@class="story_art_title"]/text()').extract_first()
		content_phrase = response.xpath('//div[@id="story_body_content"]/span/p/text() | //div[@id="story_body_content"]/span/p/a/strong/text()').extract()
		contents = '\n'.join(content_phrase)
		#print(contents)
		#for content in contents:
			#print(content)
		#	content_list.append(content.xpath('p/text()').extract_first())


		item = response.meta['item']
		item['content'] = contents

		yield item

		#item['title'] = content
	