# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from tools.models import cr_nba

class FullspiderItem(DjangoItem):
    django_model = cr_nba
