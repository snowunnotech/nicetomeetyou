from news.models import News
from news.serializers import NewsSerializer
from rest_framework import viewsets
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# from django.http import HttpResponse
# from rest_framework.permissions import IsAuthenticated


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = (IsAuthenticated,)


nbaUrl = 'https://nba.udn.com'


class New:
    def __init__(self, title, imgUrl, time, payload, url):
        self.title = title
        self.imgUrl = imgUrl
        self.time = time
        self.payload = payload
        self.url = url


def soupNews(element):
    return New(
        title=element.find('h3').string,
        imgUrl=element.find('img').get('src'),
        time=element.find('b').string,
        payload=element.find('p').string,
        url=nbaUrl + element.find('a').get('href')
    )


def news_spider():
    res = requests.get('https://nba.udn.com/nba/index?gr=www')
    soup = BeautifulSoup(res.text, 'html.parser')

    news = soup.find('div', id='news')
    array = news.find_all('dt')

    results = []
    for element in array:
        if element.find('style'):
            break
        results.append(soupNews(element))
    get_or_create_in_news_table(results)
    return results


def get_or_create_in_news_table(news_array):
    for news in news_array:
        News.objects.update_or_create(
            title=news.title,
            defaults={
                'title': news.title,
                'imgUrl': news.imgUrl,
                'time': news.time,
                'url': news.url,
                'payload': news.payload
            }
        )


def news_view(request):
    results = news_spider()
    news = News.objects.all().order_by('id')
    return render(request, 'hello.html', locals())
