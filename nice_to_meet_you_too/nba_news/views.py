from django.shortcuts import render
from rest_framework import viewsets
from nba_news.models import NbaNews
from nba_news.serializers import NbaNewsSerializer
from django.shortcuts import render

class NbaNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NbaNews.objects.all()
    serializer_class = NbaNewsSerializer

def homepage(request):
    return render(request, 'index.html')

def storypage(request, news_id):
    return render(request, 'story.html', {'news_id': news_id})

