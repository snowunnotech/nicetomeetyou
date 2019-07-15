from django.shortcuts import render
from nba_web.models import News
from nba_web.serializers import NewsSerializer
from rest_framework import viewsets


# def news_list(request):
#     return render(request, 'news.html', {})


def all_new_list(request):
    # 抓取model資料
    all_news = News.objects.all().order_by('-update_time').distinct()
    return render(request, 'all_news.html', {'news': all_news})


def news_list(request, id):
    news = News.objects.get(id=id)
    return render(request, 'news.html', locals())



# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

