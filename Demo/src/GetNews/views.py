#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from GetNews.apps import showNews
from GetNews.models import News,updateNewsWithSnake
from GetNews.Serializers import NewsSerializer
from rest_framework import viewsets, status
from rest_framework.exceptions import MethodNotAllowed

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-time')
    serializer_class = NewsSerializer
    http_method_names = ['get']

# Create your views here.
def home(request):
    return HttpResponse("<p>Hello world!</p>")
    
def ShowNews(request):
    Msg = showNews()
    return HttpResponse(Msg)
    
def UpdateNews(request):
    Msg = updateNewsWithSnake()
    return HttpResponse(Msg)
    
def NewList(request):
    #unit = News.objects.all().filter(Serial='3600718',group_id='6780')
    #print(len(unit))
    return render(request,'NBA_News.html',locals())


 