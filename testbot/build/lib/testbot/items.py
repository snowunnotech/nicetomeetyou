# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy
from scrapy_djangoitem import DjangoItem
from crawler.models import nba_news

class TestbotItem(DjangoItem):
    django_model = nba_news

