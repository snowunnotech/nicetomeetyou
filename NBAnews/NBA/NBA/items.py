# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 使用DjangoItem
from scrapy_djangoitem import DjangoItem

# Django設定的model
from main.models import imgnews

# 爬蟲數據會依django model格式 設定


class NbaItem(DjangoItem):
    django_model = imgnews

    # # 輸出json檔格式
    # class NbaItem(scrapy.Item):
    #     title = scrapy.Field()
    #     content = scrapy.Field()
    #     time = scrapy.Field()
