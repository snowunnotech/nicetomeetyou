from django.shortcuts import render
from nba_web.models import News
from nba_web.serializers import NewsSerializer

# Create your views here.
from rest_framework import viewsets


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
