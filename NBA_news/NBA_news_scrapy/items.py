# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import sys 
import os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')

# Use Module "scrapy_djangoitem" to connect django
from scrapy_djangoitem import DjangoItem
from NBAsite.models import NewsInfo

class NbaNewsScrapyItem(DjangoItem):

    django_model = NewsInfo