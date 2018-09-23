# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from nbanews.models import NbaNews
from scrapy_djangoitem import DjangoItem


class NbacrawlerItem(DjangoItem):
    django_model = NbaNews
