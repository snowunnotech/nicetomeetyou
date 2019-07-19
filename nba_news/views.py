from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from bs4 import BeautifulSoup
import requests, datetime, json
from . models import News
from . serializers import NewsSerializer
from rest_framework import viewsets
from rest_framework.decorators import list_route

##apscheduler
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler.start()

def time_task():
    a = crawler()
    res = a.write_in_db()
    print({'data':res})

scheduler.add_job(time_task, "cron", id='uni', minute=0, misfire_grace_time=30)
register_events(scheduler)

##crawler
class crawler():
    def __init__(self):
        self.home_url = 'https://nba.udn.com/nba/index?gr=www'
        self.news_url = self.get_news_url()

    def get_soup(self, url):
        res = requests.get(url)
        return BeautifulSoup(res.text, 'html.parser')

    def get_news_url(self):
        more_tag = self.get_soup(self.home_url).find('a', class_='more').get('href')
        news_url = 'http://nba.udn.com' + more_tag
        return news_url

    def get_news(self, page:int):
        dt_tag = self.get_soup(self.news_url).find('div', id='news_list_body').find('dl').find_all('dt')
        news_list = []
        for item in dt_tag:
            title = item.find('h3').string
            url = 'http://nba.udn.com' + item.find('a').get('href')
            detail = self.get_contents(url)
            news_list.append( {
                'title':title,
                'url':url,
                'news_time':detail['news_time'],
                'author':detail['author'],
                'contents':detail['contents']} )
        return news_list

    def get_contents(self, url):
        soup = self.get_soup(url=url)
        news_time = soup.find('div',class_='shareBar__info--author').find('span').string
        author = soup.find('div',class_='shareBar__info--author').text.split(' ')[3]
        tmp_contents = soup.find('div',id='story_body_content').find_all('p')[1:]
        contents = ''
        for item in tmp_contents:
            contents = contents + item.text
        detail={
            'news_time':news_time,
            'author':author,
            'contents':contents
        }
        return detail
    
    def write_in_db(self):
        news_list = self.get_news(0)
        finish = []
        for item in news_list:
            if len(News.objects.filter(title=item['title'])) == 0:
                News.objects.create(
                    title=item['title'],
                    author=item['author'],
                    news_time=datetime.datetime.strptime(item['news_time'],'%Y-%m-%d %H:%M'),
                    contents=item['contents'],
                    url=item['url'])
                finish.append(item['title'])
        return finish

##ViewSet
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @list_route(methods=['get'])
    def show(self, request):
        news_list = News.objects.all()
        res = []
        for item in news_list:
            dic = {
                'title':item.title,
                'author':item.author,
                'contents':item.contents,
                'news_time':item.news_time.strftime('%Y-%m-%d %H:%M'),
                'url':item.url
            }
            res.append(dic)
        response = HttpResponse(json.dumps({"data":res}))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

    @list_route(methods=['get'])
    def spider(self, request):
        a = crawler()
        res = a.write_in_db()
        return JsonResponse({'data':res})
