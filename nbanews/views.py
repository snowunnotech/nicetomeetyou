import re
import urllib3
import certifi
from bs4 import BeautifulSoup
from nbanews.models import News
from rest_framework import viewsets
from django.shortcuts import render
from nbanews.serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class Crawler():
    def request(self):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        content = http.request('GET', 'https://nba.udn.com/nba/index?gr=www')
        soup = BeautifulSoup(content.data, "html.parser")
        news = soup.find(class_=re.compile('^box_body')).find_all('a')
        for tag in news:
            try:
                story = self.get_story(tag.get('href'))
                news_id = story['pid']
                news_title = story['title']
                news_time = story['time']
                news_author = story['author']
                news_img = story['img']
                news_context = story['context']
                try:
                    News.objects.get_or_create(
                        pid=news_id,
                        title=news_title,
                        time=news_time,
                        author=news_author,
                        img=news_img,
                        context=news_context,
                    )
                except False:
                    pass

            except TypeError:
                pass

    def get_story(self, href):
        story = {}
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        content = http.request('GET', 'https://nba.udn.com'+href)
        soup = BeautifulSoup(content.data, "html.parser")
        parser = soup.find(id=re.compile('^story_body_content'))
        story['pid'] = href[-7:]
        story['title'] = parser.find('h1').text
        story['time'] = parser.find(class_=re.compile('^shareBar__info--author')).find('span').text
        story['author'] = parser.find(class_=re.compile('^shareBar__info--author')).find(string=re.compile('^\D'))
        story['img'] = parser.find_all('span')[2].find('img').get('data-src')
        article = []
        context = parser.find_all('p')
        for paragraph in context[1:]:
            article.append(paragraph.text)
        article = '\n'.join(article)
        story['context'] = article

        return story

get = Crawler()
get.request()

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class get_news(APIView):
    def get(self, request):
        news = News.objects.all().order_by('-pid')
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
class get_details(APIView):
    def get(self, request, pk):
        detail = News.objects.get(pid=pk)
        serializer = NewsSerializer(detail)
        return Response(serializer.data)

def target_html(request):
    return render(request, 'news.html')

def get_story(request, pk):
    story = News.objects.get(pid=pk)
    return render(request, 'story.html',{
        'data': story,
    })

