from django.shortcuts import render
from .models import News
# from news.serializers import NewsSerializer
# from rest_framework import viewsets

def home(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {
        'news_list': news_list,
    })

def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'news.html', {'news': news})
# class NewsViewSet(viewsets.ModelViewSet):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
