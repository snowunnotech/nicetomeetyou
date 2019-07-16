from django.shortcuts import render
from news.models import News
from news.serializers import NewsSerializer, DetailSerializer
from rest_framework import viewsets
from nba import settings


# Create your views here.
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-published_time')
    serializer_class = NewsSerializer


class DetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = DetailSerializer


def home(request):
    return render(request, "home.html", context={"total": settings.SERVER_IP +"nba/api/news/", "single":settings.SERVER_IP +"nba/detail/"})


def detail(request,id):
    return render(request,"detail.html", context={"total": settings.SERVER_IP +"nba/api/detail/", "id": id, "single":settings.SERVER_IP +"nba/api/detail/"})
