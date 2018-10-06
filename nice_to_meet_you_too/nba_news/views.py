from django.shortcuts import render
from rest_framework import viewsets
from nba_news.models import NbaNews
from nba_news.serializers import NbaNewsSerializer

class NbaNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NbaNews.objects.all()
    serializer_class = NbaNewsSerializer
