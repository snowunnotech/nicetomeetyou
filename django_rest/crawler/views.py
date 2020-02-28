from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import time
from rest_framework import viewsets
from .serializers import nba_newsSerializer
from .models import nba_news



def simple_crawl(request):
    # url = "https://nba.udn.com/nba/index?gr=www"
    # res = requests.get(url)
    # soup = BeautifulSoup(res.text,"html.parser")
    # for news in soup.find('div', id='news_body').find_all('dt'):
    #     if news.find('h3'):
    #         news_title=news.find('h3').text

    #         news_url='https://nba.udn.com'+news.find('a').get('href')

    #         pre_time=''.join([x for x in news.find('b').text if x.isdigit()])
    #         if '小時' in news.find('b').text:
    #             news_time=time.strftime("%Y/%m/%d, %H:%M", time.localtime(time.time()-int(pre_time)*60*60+8*60*60))
    #         elif '分鐘' in news.find('b').text:
    #             news_time=time.strftime("%Y/%m/%d, %H:%M", time.localtime(time.time()-int(pre_time)*60+8*60*60))
    #         else:
    #             news_time=time.strftime("%Y/%m/%d, %H:%M", time.localtime(time.time()-int(pre_time)+8*60*60))

    #         res1 = requests.get(news_url)
    #         soup1 = BeautifulSoup(res1.text,"html.parser")
    #         list = []
    #         for p in soup1.select('#story_body_content p')[:-1]:
    #             list.append(p.text.strip())
    #         news_content = ' '.join(list)



    #     if nba_news.objects.filter(nba_url=news_url).exists():
    #         continue
    #     else:
    #         nba_news.objects.create(nba_title=news_title,nba_content=news_content,nba_time=news_time,nba_url=news_url) 
    all_nba_news = nba_news.objects.all().order_by('-nba_time')

    return render(request,'simple_crawl.html',locals())
    



def detail_news(request, slug):
    nbanews = nba_news.objects.get(slug = slug)
    context = {
        'nba_news' : nbanews
    }
    return render(request, 'show_news.html', context)

class nba_newsViewSet(viewsets.ModelViewSet):
    queryset = nba_news.objects.all().order_by('-nba_time')
    serializer_class = nba_newsSerializer