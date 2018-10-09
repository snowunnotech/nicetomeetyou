# -*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import datetime
from nba_news.models import NewsTable
from nba_news.serializers import NewsTableSerializer

from rest_framework import viewsets


from bs4 import BeautifulSoup as bs4
import requests

# Create your views here.

class NewsTableViewSet(viewsets.ModelViewSet):
    queryset = NewsTable.objects.all()
    serializer_class = NewsTableSerializer

def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "Hello Django ",
    })

def index(request):
	data = NewsTable.objects.all().order_by('id')[:3]
	# news_data = nba_cralwer()
	return render(request, 'index.html', {
		'current_time': str(datetime.now()),
		'data': data,
	})
def nba_cralwer():
	news_data = []
	all_news_id = [ info['news_id'] for info in NewsTable.objects.all()]
	result = requests.get('https://nba.udn.com/nba/index?gr=www')

	if(result.ok):
		news_content = result.content
		soup = bs4(news_content, "html.parser")
		dts = soup.select('div#news_body > dl > dt')
		for dt in dts:
			detail_data = {}
			if not (dt.get('class') and (dt.get('class')[0]=='ads')):
				title = dt.a.h3.text
				url = "https://nba.udn.com"+dt.a.get('href')
				img_url = dt.find("span", {"class": "img-boxs"}).img.get('src').split('&')[0]
				news_id = url.split('/')[-1]
				if news_id not in all_news_id:
					detail_result = requests.get(url)
					if(detail_result.ok):
						detail_content = detail_result.content
						detail_soup = bs4(detail_content, "html.parser")
						detail_body = detail_soup.find("div", {"id":"story_body_content"})
						detail_title = detail_body.find("h1", {"class" : "story_art_title"}).text
						detail_time = detail_body.find("div", {"class" : "shareBar__info--author"}).span.text
						detail_date  = datetime.strptime(detail_time, '%Y-%m-%d %H:%M')
						detail_news_block = detail_body.find_all("span")[2]
						detail_news = detail_news_block.find_all("p")
						if detail_news:
							detail_news_text = '\n'.join([p.text for p in detail_news[1:-1] if (p.text)])
							detail_data = {'news_id':news_id, 'title':title, 'url':url, 'img_url':img_url, 'time':detail_date, 'news_text':detail_news_text}
							news_data.append(detail_data)
	# 			else:
	# 				print("Connect News Detail Page Error!! HTTP Status: ",result.status_code)
	# else:
	# 	print("Connect Main News Page Error!! HTTP Status: ",result.status_code)
	if(news_data):
		for data in news_data:
			update_news =  NewsTable.objects.create(news_id=data['news_id'], title=data['title'], url=data['url'], img_url=data['img_url'], time=data['time'], news_text=data['news_text'])
			update_news.publish()
	# return(news_data)
