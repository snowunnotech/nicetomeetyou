# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class News(models.Model):

    title = models.TextField(default="test_news")
    author = models.TextField(default="zihan")
    content = models.TextField(default="test_news")
    news_url = models.TextField(default="http://", unique=True)
    org_news_date = models.DateTimeField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"