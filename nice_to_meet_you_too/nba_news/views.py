from django.shortcuts import render
from rest_framework import viewsets
from nba_news.models import NbaNews
from nba_news.serializers import NbaNewsSerializer
from django.shortcuts import render
from django.forms.models import model_to_dict

class NbaNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NbaNews.objects.all()
    serializer_class = NbaNewsSerializer

def homepage(request):
    return render(request, 'index.html')

def storypage(request, news_id):
    news = NbaNews.objects.get(id = news_id)
    dict_render = model_to_dict(news)
    dict_render['created'] = 'Today'
    return render(request, 'story.html', dict_render)

