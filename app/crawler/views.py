from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
import os

from .services import *
from helper.helper import APIHandler
# Create your views here.

class Hello(APIView):
    def get(self, request):
        return Response('Hello world.')

class Nba_Crawler(APIView):
    def post(self, request):
        url = os.getenv('NBA_URL')
        zip_data = CRAW(url)
        new_news_ids = []
        for data in zip_data:
            news_state = CHECK_EXIST(data)
            if news_state:
                continue
            else:
                news_id = SAVE_NEWS(data)
                new_news_ids.append(news_id)
        if new_news_ids:
            return APIHandler.catch(data={'news_ids':new_news_ids}, code='001')
        else:
            return APIHandler.catch(data='Nothing new', code='000')

