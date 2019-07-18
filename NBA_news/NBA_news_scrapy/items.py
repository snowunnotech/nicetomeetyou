# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy

import sys 
import os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')

from scrapy_djangoitem import DjangoItem
from NBAsite.models import NewsInfo

class NbaNewsScrapyItem(DjangoItem):
    # define the fields for your item here like:
    #title = scrapy.Field()
    #image = scrapy.Field()
    #content = scrapy.Field()
    #time = scrapy.Field()
    django_model = NewsInfo