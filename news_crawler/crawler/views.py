from crawler.models import News
from crawler.serializers import NewsSerializer
from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import DetailView
from django.http import HttpResponseNotFound

# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

def newsDetail(request, pk):
    try:
        p = News.objects.get(news_id=pk)
    except News.DoesNotExist:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    return render(request, 'news_detail.html', {'news_id': pk})

def homepage(request):
    return render(request, 'index.html')
