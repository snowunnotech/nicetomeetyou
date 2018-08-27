import scrapy
from urllib.parse import urljoin
from newsbot.items import NewsbotItem

class NewsSpider(scrapy.Spider):
    name = "news_spider"
    start_urls = [
        'https://nba.udn.com/nba/index?gr=www',
    ]

    def parse(self, response):
        nbody = response.css('#news_body')
#        print('-------------------------------------')
#        print(nbody)
#        print(nbody.css('dt'))
#        print('-------------------------------------')
        for quote in nbody.css('dt')[::-1]:
            if quote.css('a::attr(href)').extract() != []:
                item = NewsbotItem()
#                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                item['link'] = urljoin('https://nba.udn.com',quote.css('a::attr(href)').extract()[0])
                item['photo'] = quote.css('span img::attr(src)').extract()[0]
                item['headline'] = quote.css('a h3::text').extract()[0]
                item['body'] = quote.css('a p::text').extract()[0]
                yield item
