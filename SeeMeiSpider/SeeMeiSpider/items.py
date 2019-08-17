# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from index.models import Feeds, News, NewsDetail


class SeemeispiderItem(DjangoItem):
    django_model = Feeds

class NewsItem(DjangoItem):
    django_model = News

class NewsDetailItem(DjangoItem):
    django_model = NewsDetail
