# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from newsboard.models import NewsArticle

class NbaNewsItem(DjangoItem):
    django_model = NewsArticle