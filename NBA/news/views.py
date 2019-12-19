from django.shortcuts import render
from django.conf import settings

from .serializers import NBANewsSerializer 
from .models import NBANews

from rest_framework import viewsets

# Create your views here.


class NBANewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NBANews.objects.all().order_by('-published')
    serializer_class = NBANewsSerializer

def news_list(request):
    context = {
        'url': settings.SERVER_IP + "nba/api/news/",
    }
    return render(request, 'news/list.html', context=context)

def news_detail(request, news_id):
    context = {
            'url': settings.SERVER_IP + "nba/api/news/",
        'id': news_id,
    }
    return render(request, 'news/detail.html', context=context)
