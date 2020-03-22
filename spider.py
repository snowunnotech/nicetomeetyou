import scrapy
from pprint import pprint


class Spider(scrapy.Spider):
    name = "nba"
    start_urls = [
        'https://nba.udn.com/nba/index?gr=www'
    ]

    def parse(self, response):
        hot_list = response.xpath('//div[@id="mainbar"]/a/text()').getall()
        for l in hot_list:
            pprint(l)