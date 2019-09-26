# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class NewsItem(scrapy.Item):
    title = Field()
    pub_time = Field()
    content = Field()
