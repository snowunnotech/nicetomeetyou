# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from pyscraper.models import Article, Headline
from scrapy_djangoitem import DjangoItem


class HeadlineItem(DjangoItem):
    django_model = Headline


class ArticleItem(DjangoItem):
    django_model = Article
    # define the fields for your item here like:
    # name = scrapy.Field()
