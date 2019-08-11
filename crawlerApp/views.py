from django.shortcuts import render
from crawlerApp.models import News
from crawlerApp.serializers import NewsSerializer


from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import time
import lxml
import requests
from bs4 import BeautifulSoup

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

# Create your views here.

# crawler every 2 hour
try:
	scheduler = BackgroundScheduler()
	scheduler.add_jobstore(DjangoJobStore(), "default")
	@register_job(scheduler,"interval", seconds=60*60*2)
	def my_job():
		url = 'https://nba.udn.com/nba/news/'
		resp = requests.get(url)
		soup = BeautifulSoup(resp.text, 'html.parser')
		news_block = soup.find("div", {"id":"news_list_body"}).find_all("a")

		for new in news_block:
			href = ''.join(["https://nba.udn.com", new.get('href')])
			title = new.find("h3").text
			outline = new.find("p").text

			resp_new = requests.get(href)
			selector = lxml.etree.HTML(resp_new.text)
			content_phrase = selector.xpath('//div[@id="story_body_content"]/span/p/text() | //div[@id="story_body_content"]/span/p/a/strong/text()')
			contents = '\n'.join(content_phrase)
			
			#store into db
			newObject = News.objects.get_or_create(title=title, href=href, outline=outline, content=contents )

			print("Update the DB~")
		pass
	register_events(scheduler)
	scheduler.start()
except Exception as e:
	print(e)
	scheduler.shutdown()


@api_view(['GET'])

def news_list(request):
	if request.method == 'GET':
		#news = News.objects.filter(board__exact = 'NBA', date__lt = '2018/03/01', date__gt = '2018/02/01').order_by('-title')[:5]
		#news = News.objects.raw("SELECT * FROM crawlerApp_news LIMIT 100")
		news = News.objects.all()[:100]
		serializer = NewsSerializer(news, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def new(request, newId=None):
	if(newId):
		#new = News.objects.filter(id_exact = newId)
		#new = News.objects.raw("SELECT * FROM crawlerApp_news WHERE `id` = %s", [newId])
		new = News.objects.all()
		serializer = NewsSerializer(new, many=True)
		return Response(serializer.data[0])


def showNews(request):


	return render(request, "news.html", locals())

def showANew(request, newId=None):

	return render(request, "new.html", locals())
