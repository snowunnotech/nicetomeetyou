# -*- coding: utf-8 -*-
import scrapy
from ..items import CrawlerItem

import requests

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['https://nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/index?gr=www']
    autoUpdate = True
    postUrl = 'http://localhost:8000/api/'
    headers = {'content-type': 'application/json'}

    def parse(self, response):
        items = CrawlerItem()
        for q in response.css('div.box_body'):
            for x in q.css('dt'):
                data = {}
                items['title'] = x.css('a > h3::text').extract_first()
                items['href'] = x.css('a::attr(href)').extract_first()
                items['context'] = x.css('a > p::text').extract_first()
                if self.autoUpdate:
                    data['title'] = items['title']
                    data['href'] = 'https://nba.udn.com' + items['href']
                    data['context'] = items['context']
                yield(items)
                if data['title'] != None:
                    requests.post(self.postUrl, data=data)
            break

