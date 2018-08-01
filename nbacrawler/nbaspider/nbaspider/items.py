# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NbaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # list
    # url = scrapy.Field()
    # detail
    title = scrapy.Field()
    publish_date = scrapy.Field()
    author = scrapy.Field()
    image_url = scrapy.Field()
    image_caption = scrapy.Field()
    video_url = scrapy.Field()
    content = scrapy.Field()
