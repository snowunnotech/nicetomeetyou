'''
Created on Oct 20, 2018

@author: s0974129
'''

import requests
from bs4 import BeautifulSoup
from nbanews.loggers import logger
#rest framework
from news.newsSerializers import newsSerializer
from news.models import News
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
#web socket use
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer



class newsViewSet(
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet ):
    '''
        table : news
        
        '/' - get : 查詢資料
        
        '/{id}/' - get : 檢視
        
        '/refresh/' - post : 重新整理(發送websocket)
        
    '''

    queryset = News.objects.all()
    #use create serializer because of api web page
    serializer_class = newsSerializer
    
    def retrieve(self, request, *args, **kwargs):
        
        id = kwargs['pk']
        
        newsData = News.objects.get( id = id )
        
        detailsrc = newsData.detailsrc
        
        result = {}
        #抓取焦點新聞的詳細資料。
        try :
                                
            response = requests.get( 'https://nba.udn.com' + detailsrc, timeout = 5 )
            
            soup = BeautifulSoup( response.text, 'html.parser')
            #找新聞區塊
            newsBody = soup.find(id='story_body_content')
            #找標題
            result['title'] = newsBody.find('h1').text
            #j找文章資訊
            result['info'] = newsBody.find('div', 'shareBar__info--author').text
            #找圖片
            result['imgsrc'] = newsBody.find('img')['data-src']
            #找內容
            contentData = newsBody.find_all('p')[1:]
            
            contentText = ''
            for content in contentData :
                
                contentText = contentText + content.text 
                
            result['content'] = contentText           
        
            #logger.debug( result )
            
        except Exception as e:
             
            logger.warning( 'error : %s :' % e )
             
            result['errorMessage'] = 'error : %s :' % e
         
        finally:
        
            return Response( result )
        
    @action( methods=[ 'post' ], detail=False)
    def refresh(self, request ):
        
        '''
            refresh : send websocket
        '''
        
        #送web socket(call url)
        channelLayer = get_channel_layer()
        #送websocket到首頁(refresh)
        async_to_sync(channelLayer.group_send)( 'index', {'type' : 'chat_message', 'message' : 'refresh' } )
        
        return Response( True )
    
    
    



