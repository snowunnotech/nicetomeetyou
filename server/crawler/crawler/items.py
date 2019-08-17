# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from api.models import HotNews


# class CrawlerItem(scrapy.Item):
#     title = scrapy.Field()
#     content = scrapy.Field()
#     image_url = scrapy.Field()
#     post_date = scrapy.Field()


class CrawlerItem(DjangoItem):
    django_model = HotNews