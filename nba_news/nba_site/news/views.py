from django.shortcuts import render_to_response, render
from news.serializers import NewsListSerializer, NewsDetailSerializer
from news.models import News
from rest_framework import viewsets

# Create your views here.
def news_view(request):
    news = News.objects.all().order_by('-id')  # 依據id欄位遞減排序顯示所有資料
    return render(request, 'nba_news.html', locals())


def content_view(request):
    content = News.objects.get(id=request.GET['id'])
    return render_to_response('content.html', locals())


def news_list_api(request):
	return render(request, "news_list_api.html")


def news_detail_api(request):
	return render(request, "news_detail_api.html")


class NewsListViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetailViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer