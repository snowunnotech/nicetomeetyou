from django.shortcuts import render,redirect, get_object_or_404 # 9/25引入404
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.template import loader, RequestContext # 其實 render就已經封裝好了
from myapp.models import member,articles,visit_num  # 引入models內的member
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # 顯示頁數
from django.db.models import Q  # 使用 OR and 等
import json
from django.views.decorators.csrf import csrf_exempt
from nba_news.models import News
# 顯示介面要輸出之文字
# 1.定義Views函數, HttpResponse
# 2.進行urls配置，建立url地址和views的對應關係
# 3.產生html內容
# 4.返回html給browser

from bs4 import BeautifulSoup
import requests
import html5lib
def get_web(url):
	web = requests.get(url)
	if web.status_code == 200:
		return web.text
	else:
		return "出現錯誤囉!!"


def nba_news(request):
	from nba_news.crawel import main
	data = main()
	return render(request, 'nba_news/nba_news.html', locals(),)


@csrf_exempt
def getnews_detail(request):
	if request.method == 'POST':
		res_data = {}
		res_data['status'] = "success"
		data = json.loads(request.body)
		title = data['title']
		href = data['href']
		## 抓取內容
		web = get_web(href)
		web_content = BeautifulSoup(web,'html5lib')
		span = web_content.find('div',id="story_body_content").find_all("span")[2]
		p_all = span.find_all("p")
		string = ""
		for p in p_all:
			string+= p.text
		## 放到資料庫
		new_items = News()
		new_items.Title = title
		new_items.Href = href
		new_items.Content = string
		new_items.save()
		res_data['content'] = string
	return JsonResponse(res_data)
