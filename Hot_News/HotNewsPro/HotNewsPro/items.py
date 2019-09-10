# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from HotNew.models import HotNews
# from scrapy.contrib.djangoitem import DjangoItem

class HotnewsproItem(DjangoItem):
    # define the fields for your item here like:
    # title = scrapy.Field()
    # url = scrapy.Field()

    # title = HotNews
    # url = HotNews

    django_model = HotNews

