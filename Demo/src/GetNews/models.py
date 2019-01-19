#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from GetNews.apps import getNewsPublishTime,getNewsUrl,getNewsRawData

class News(models.Model):
    Serial = models.CharField(max_length=256, verbose_name='流水號')
    group_id = models.CharField(max_length=256, verbose_name='組序號')
    img_url = models.CharField(max_length=256, verbose_name='圖片網址')
    news_url = models.CharField(max_length=256,default='', verbose_name='新聞網址')
    title = models.CharField(max_length=50, verbose_name='標題')
    content = models.TextField(verbose_name='簡述')
    time = models.DateTimeField(verbose_name='發表時間')
    def __str__(self):
        return self.Serial + '/' + self.group_id + '  ' + self.title
        
def updateNewsWithSnake():

    basicUrl = 'https://nba.udn.com/'
    RawData = getNewsRawData()
    print('=======UpdateNews=======')
    for item in RawData:
        _Serial = str(item.a['href']).split('/')[4]
        _group_id = str(item.a['href']).split('/')[3]
        _title = str(item.h3.text)
        _news_url = str(basicUrl  +  str(item.a['href']))
        _content = str(item.p.text)
        _img_url = str(item.img['data-src'])
        _time = getNewsPublishTime(basicUrl+ str(item.a['href']))
        if(isExistNews(_Serial,_group_id)):
            print(_group_id+'/'+_Serial + ' is Exist')
        else:
            print(_group_id+'/'+_Serial + ',Time:' +_time + ' is new')
            add = News(Serial=_Serial, group_id=_group_id,img_url=_img_url,
            news_url=_news_url,title=_title,content=_content,time=_time)
            add.save()
    print('=======UpdateNews_Ending=======')
    return 'UpdateFinish'
    
def isExistNews(_serial,_group_id):
    unit = News.objects.all().filter(Serial=str(_serial),group_id=str(_group_id))
    if(len(unit)>0):
        return True
    else:
        return False