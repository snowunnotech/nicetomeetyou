# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class UdnNbaItem(Item):
    id = Field()
    title = Field()
    url = Field()
    author = Field()
    contents = Field()
    published_datetime = Field()