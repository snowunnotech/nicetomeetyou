# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import ArticlespiderItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        urls = response.css("#news dt a::attr(href)").extract()
        for url in urls:
            request_url = 'https://nba.udn.com'+url
            yield scrapy.Request(request_url, callback=self.parse_details)

    def parse_details(self, response):
        item_loader = ItemLoader(item=ArticlespiderItem(),response=response)
        item_loader.add_css('title', '#story_body_content h1::text')
        item_loader.add_css('image_url', '#story_body_content figure img::attr(data-src)')
        item_loader.add_css('content', '#story_body_content span p::text')
        item_loader.add_css('published_time', '.shareBar__info--author > span:nth-child(1)::text')
        loaded_item = item_loader.load_item()
        yield loaded_item
