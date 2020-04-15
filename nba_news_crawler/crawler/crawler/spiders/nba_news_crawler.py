import scrapy
from urllib.parse import urljoin
from crawler.items import NbaNewsItem


class Crawler(scrapy.Spider):
    name = 'nba_news_crawler'
    start_urls = ['https://nba.udn.com/nba/index?gr=www']
    HOST = 'https://nba.udn.com'

    def parse(self, response):
        news = response.css("#news_body dl dt a")
        for current_news in news:
            item = NbaNewsItem()
            relative_url = current_news.css('::attr(href)').extract_first()
            item['url'] = urljoin(self.HOST, relative_url)
            item['image'] = current_news.css('img::attr(src)').extract_first()
            item['title'] = current_news.css('h3::text').extract_first()
            yield item
