# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
import scrapy

from chat.models import Udn

    # name = scrapy.Field()
class ScrapyudnItem(scrapy.Item):
    title=scrapy.Field()
    link=scrapy.Field()
    report=scrapy.Field()
    content=scrapy.Field()
    time=scrapy.Field()
    django_model = Udn
    # name = scrapy.Field()
