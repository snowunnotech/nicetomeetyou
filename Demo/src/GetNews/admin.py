#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.contrib import admin

# Register your models here.

from GetNews.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display=('Serial','group_id','title','news_url','time')
    list_filter=('Serial','group_id')
    search_fields=('title',)
    ordering=('-time',)
    
admin.site.register(News,NewsAdmin)
