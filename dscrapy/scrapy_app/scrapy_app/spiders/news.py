# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider


class NewsSpider(CrawlSpider):
    name = 'news'
    start_urls = ['https://nba.udn.com/nba/index?gr=www/']

    def parse(self, response):
        item = {}
        for news in response.css("#news_body a"):
            item['link_url'] = response.urljoin(news.css("a::attr(href)").get())
            item['title'] = news.css("h3::text").get()
            item['img_url'] = news.css("img::attr(src)").get()
            yield item
        
