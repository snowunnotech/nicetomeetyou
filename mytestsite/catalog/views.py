from django.shortcuts import render
from rest_framework import generics
from .serializers import NewsSerializer
from .models import NBASpotNews
from django.http import HttpResponse
from rest_framework import viewsets
from .web_crawler import *

def index(request):
	execute_timer()
	news_list = NBASpotNews.objects.all().order_by('-report_time')
	return render(request, 'index.html', {'news_list':news_list})

def show_detail_news(request, slug):
    news_detail = NBASpotNews.objects.filter(slug = slug)[0]
    return render(request, 'news_detail.html', {'news_detail':news_detail})

class NewsViewSet(viewsets.ModelViewSet):
	queryset = NBASpotNews.objects.all()
	serializer_class = NewsSerializer