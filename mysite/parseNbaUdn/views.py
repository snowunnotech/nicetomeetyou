from django.shortcuts import render
import requests

from .models import TopNews
from .parser import TopNewsParser

# Create your views here.


def task(request):
    url = 'https://nba.udn.com/nba/index?gr=www'
    page = requests.get(url)
    p = TopNewsParser(url)
    p.feed(page.text)
    for n in p.newsList:
        try:
            TopNews.objects.get(postId=n.postId)
        except TopNews.DoesNotExist:
            TopNews(postId=n.postId, title=n.title, imgUrl=n.imgUrl, pageUrl=n.pageUrl).save()
        finally:
            pass
