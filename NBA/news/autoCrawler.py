#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#coding=utf-8
"""
Created on Mon Nov  6 17:01:36 2017

@author: wayne17
"""

import NewsCrawler
import os
# import django

# print(django.get_version())
os.system("export DJANGO_SETTINGS_MODULE=NBA.settings")
from news.models import News

html = NewsCrawler.simpleQuery()
for n in html:
    if not News.objects.filter(title__contains=n['title']):
        News.objects.create(title=n['title'], content=n['content'], detail=n["detail"], url=n["href"], pic_url=n['pic'])
