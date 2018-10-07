from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from nba_news.models import NbaNews
from nba_news.serializers import NbaNewsSerializer
from datetime import datetime
import subprocess
from django.http import HttpResponse

class NbaNewsList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = NbaNews.objects.all().order_by("-created")
    serializer_class = NbaNewsSerializer
    
    def get(self, request, *args, **kwargs):
        subprocess.run('python manage.py crawl_nba'.split())
        return self.list(request, *args, **kwargs)
    
class NbaNewsDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = NbaNews.objects.all().order_by("-created")
    serializer_class = NbaNewsSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NbaNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NbaNews.objects.all().order_by("-created")
    serializer_class = NbaNewsSerializer

def homepage(request):
    return render(request, 'index.html')

def storypage(request, news_id):
    news = NbaNews.objects.get(id = news_id)
    dict_render = model_to_dict(news)
    dict_render['created'] = 'Today'
    return render(request, 'story.html', dict_render)

def crawl(request):
    subprocess.run('python manage.py crawl_nba'.split())
    response = HttpResponse("Finsh crawling")
    return response
