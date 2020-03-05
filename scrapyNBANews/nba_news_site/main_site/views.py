from django.shortcuts import render
from main_site.models import News
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, action
from main_site.serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-post_date')
    serializer_class = NewsSerializer

@api_view(['GET'])
def newsIndex(request):
    news_list = News.objects.all().order_by('-post_date')
    return render(request, 'Index.html', {'news_list':news_list})

@api_view(['GET'])
def newsDetail(request, news_id):
    print(news_id)
    news_detail = News.objects.get(news_id=news_id)
    return render(request, 'news_detail.html', {'news_detail':news_detail})