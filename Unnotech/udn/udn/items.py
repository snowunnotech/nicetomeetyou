# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from news.models import News
from scrapy_djangoitem import DjangoItem

class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    datetime = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()

class NewsDjangoItem(DjangoItem):
    django_model = News
