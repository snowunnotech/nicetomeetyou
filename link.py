import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from ..items import newsItem
from bs4 import BeautifulSoup
import time



class NewsSpider(scrapy.Spider):
    name = "link"
    #allowed_domains= ["nba.udn.com/nba/cate/6754"]
    start_urls = ['https://nba.udn.com/nba/cate/6754']
    def parse(self, response):
        
        for i in response.css('div.box_body'):
            news= newsItem()
            news['href'] = i.xpath('./dl/dt/a/@href')
            #news['content'] = i.xpath('./dl/dt/a/@span')
            news['title']= i.css('h3::text')
            news['content']=i.css('p::text')
            print(news)
            yield news
    
        # i=0
        # next_url = response.css('div.pagelink gonext a::attr(href)').extract_first()
        # if next_url and i<2: 
        #     i=i+1 
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse)



