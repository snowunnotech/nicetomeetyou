"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from app.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from rest_framework import status
from django.core import serializers
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/index.html',
        {
            'year':datetime.now().year,
        })

@schema(None)
@api_view(['GET'])
def getnewslist(request):
    news = News.objects.only('Title','Image','Content','Url').all().order_by('-Time')
    news = serializers.serialize('json',  news)
    return Response(news)

@schema(None)
@api_view(['GET'])
def getnewsdetail(request,id=1):
    new = News.objects.only('Title','Detail').filter(id=id)
    if len(new) >0:
        new = new
        new = serializers.serialize('json',  new)
    return Response(new)


@schema(None)
@api_view(['GET'])
def getclecrawler(request):
    getweb()
    try:
        #getweb()
        SystemLog.objects.create(
            Time = datetime.now(),
            Message = 'Successful Save!'
            )
        return Response({
            'message':'Successful Save!'
            },status=status.HTTP_200_OK)
    except Exception as e:
        SystemLog.objects.create(
            Time = datetime.now(),
            Message = '抓取失敗!'+ str(e)
            )
        return Response({
            'message':'抓取失敗!'
            })

 

def getweb():
    res = requests.get('https://nba.udn.com/nba/cate/6754')
    soup = BeautifulSoup(res.text, 'html.parser')
    news = soup.find('div',id='news_list_body')
    dt = news.find_all('dt')
    for item in dt:
        url = 'https://nba.udn.com' + str(item.find('a')['href'])
        news = News.objects.filter(Url=url)
        if len(news) == 0 :
            news = News.objects.create(Title = str(item.find('h3')).replace('<h3>','').replace('</h3>',''),
                Url = url,
                Image = str(item.find('img')['data-src']),
                Content = str(item.find('p')).replace('<p>','').replace('</p>',''))
            res = requests.get(url)
            soup = BeautifulSoup(res.text, 'html.parser')
            detail = soup.find('div',id='story_body')
            detail = detail.find_all('span')
            time = str(detail[0]).replace('<span>','').replace('</span>','')
            news.Time = datetime.strptime(time, '%Y-%m-%d %H:%M')
            d = detail[2].find_all('p')
            text = ''
            a = len(d)
            for num in range(1, len(d)):
                text = text + str(d[num])
            news.Detail = text
            news.save()