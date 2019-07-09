import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import NewsInfo
from .serializers import NewsInfoSerializer
from rest_framework import viewsets
# Create your views here.


def news_index(request, id):
    p = NewsInfo.objects.get(id=id)
    return render(request, 'article.html', locals())


def homepage(request):
    news = NewsInfo.objects.all()
    return render(request, 'homepage.html', locals())


class MainSiteViewSet(viewsets.ModelViewSet):
    queryset = NewsInfo.objects.all()
    serializer_class = NewsInfoSerializer
