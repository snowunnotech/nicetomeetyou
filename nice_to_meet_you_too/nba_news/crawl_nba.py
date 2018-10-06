import scrapy
from scrapy.crawler import CrawlerProcess
import json

class NbaNewsSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://nba.udn.com/nba/index?gr=www'
    ]


    #def __init__(self, fn_to_store = 'info_scrapy_try.txt'):
    #    self.fn_to_store = fn_to_store

    def parse(self, response):
        if 'index' in response.url:
            news_list_url = response.css('a.more')[0].css('a::attr(href)').extract_first()
            yield response.follow(news_list_url, callback = self.parse)
        elif 'cate' in response.url:
            for news_url in  response.xpath('//div[@id="news_list_body"]//dt').css('a::attr(href)').extract():
                yield response.follow(news_url, callback = self. parse)
            
        """
        for news in response.xpath('//div[@id="news_body"]//dt'):
            #dict_info = {
            yield {
                'href': news.css('a::attr(href)').extract_first()
                #'text': quote.css('span.text::text').extract_first(),
                #'author': quote.css('span small::text').extract_first(),
                #'tags': quote.css('div.tags a.tag::text').extract(),
            }
            #f_to_store.write(json.dumps(dict_info))
        """
        #next_page = response.css('li.next a::attr(href)').extract_first()
        #if next_page is not None:
        #    yield response.follow(next_page, callback=self.parse)

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(NbaNewsSpider)
process.start() # the script will block here until the crawling is finished
