'''
Created on Oct 21, 2018

@author: s0974129
'''

# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task, task
from news.views import get_newsContent
from news.models import News
from nbanews.loggers import logger
import requests


@shared_task
def news_grab():
    
    newsContent = get_newsContent()
    
    #狀態 : 判斷是否有新增
    status = False
    #新增至資料庫
    for news in newsContent :
        
        createdStatus = News.objects.get_or_create(**news)[1]
        
        if createdStatus is True :
            
            status = True
    
    if status is True :
        
        #送websocket(call url)
        try :
            
            requests.post( 'http://127.0.0.1:8000/api/news/refresh/', timeout = 2 )
        
        except Exception as e :
            
            logger.warning(e)
    
    return status