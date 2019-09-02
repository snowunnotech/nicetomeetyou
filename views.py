from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import datetime
import json
import libs
import requests
import pandas as pd
from bs4 import BeautifulSoup

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from getnews.models import hotnew
import time
import os

# Create your views here.

def ajax_list(request):
	response_data = []
	for new in hotnew.objects.all():
		data = {'link':new.new_link, 'title':new.new_title}
		response_data.append(data)
			
	#return JsonResponse(response_data, json_dumps_params={'ensure_ascii':False}, safe=False)
	#return HttpResponse(json.dumps(response_data, ensure_ascii=False), content_type="application/json")
	#return render(request, 'news.html', {'response_data': json.dumps(response_data, ensure_ascii=False)})
	return render_to_response('news.html', {'response_data': json.dumps(response_data, ensure_ascii=False)})


def get_news(request):
	url = 'https://nba.udn.com/nba/index?gr=www'
	resp = requests.get(url)
	resp.encoding = 'utf-8' # encoded with format utf-8 for chinese character
	soup = BeautifulSoup(resp.text, 'lxml')
	
	rows = soup.find_all('div', class_='box')
	for row in rows:
		news_link = row.find_next('a')['href']
		break;
	
	new_url = 'https://nba.udn.com' + news_link
	#print(new_url)
	
	count = 0
	resp2 = requests.get(new_url)
	resp2.encoding = 'utf-8' # encoded with format utf-8 for chinese character
	soup2 = BeautifulSoup(resp2.text, 'lxml')
	
	news_rows = soup2.find_all('dt')
	for news_row in news_rows:
		if count > 1 and count < 12:
			link = 'https://nba.udn.com' + news_row.find_next('a')['href']
			id = link.split('/')[6]
			title = news_row.find_next('h3').string
			
			obj, created = hotnew.objects.get_or_create(new_id = id, new_title = title, new_link = link)
		count+=1

	news = hotnew.objects.all()
	return render(request, 'news.html', locals())