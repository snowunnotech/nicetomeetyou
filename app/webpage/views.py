from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.apps import apps
from .services import *
import json

# Create your views here.

class NBA_News_In_Focus(APIView):
    def get(self,request):
        news_in_focus = GET_NBA_NEWS(items=5)
        news_list = []
        for obj in news_in_focus:
            news_dic = {
                'title': obj.title,
                'intro': obj.intro,
                'link': obj.link,
                'content': obj.content,
                'id': obj.id,
            }
            news_list.append(news_dic)
        return render(request, 'NBA_homepage.html', {'news_in_focus':news_in_focus})

class NBA_News_In_Focus_List(APIView):
    def get(self,request):
        news_in_focus = GET_NBA_NEWS(items=5)
        news_list = []
        for obj in news_in_focus:
            news_dic = {
                'title': obj.title,
                'intro': obj.intro,
                'link': obj.link,
                'content': obj.content,
                'id': obj.id,
            }
            news_list.append(news_dic)
        return Response(news_list)

class NBA_News_Detail(APIView):
    def get(self,request,id):
        obj = GET_NBA_NEWS_BYID(id=id)
        if not obj:
            return Response('No news')
        else:
            news_detail = {
                'title': obj.title,
                'link': obj.link,
                'content': obj.content,
            }
        return render(request, 'NBA_news_detail.html', {'news_detail':news_detail})

