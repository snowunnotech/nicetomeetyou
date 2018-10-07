from django.shortcuts import render
from rest_framework import viewsets
from nba_news.models import NbaNews
from nba_news.serializers import NbaNewsSerializer
from django.shortcuts import render
from django.forms.models import model_to_dict
from datetime import datetime
import subprocess

newest_title = NbaNews.objects.all().order_by("-id")[0].title

class NbaNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NbaNews.objects.all()
    serializer_class = NbaNewsSerializer

def homepage(request):
    #subprocess.run('python ../manage.py crawl_nba'.split())
    subprocess.run('python manage.py crawl_nba --title {0}'.format(newest_title[:5]).split())
    return render(request, 'index.html')

def storypage(request, news_id):
    news = NbaNews.objects.get(id = news_id)
    dict_render = model_to_dict(news)
    dict_render['created'] = 'Today'
    return render(request, 'story.html', dict_render)

