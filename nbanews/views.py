from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Articles
from rest_framework import viewsets
from .serializers import ArticlesSerializer

#顯示爬蟲到的新聞
def news(request):
	return render(request, 'news.html',{})
#負責抓取資料
def home(request):
	url = 'https://nba.udn.com/nba/index?gr=www'
	res = requests.get(url)
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text, 'html.parser')

	#新聞內容
	stext = soup.select('#news_body p')
	texts =[]
	for text in stext:
		texts.append(text.contents[0])

	#新聞標題
	stitle = soup.select('#news_body h3')
	titles =[]
	for title in stitle:
		titles.append(title.contents[0])
	#新聞連結
	base_link = 'https://nba.udn.com'
	sdetail = soup.select('#news_body a ')
	details = []
	for detail in sdetail:
		details.append(base_link +detail.get('href'))
	#時間
	stime = soup.select('#news_body dt b')
	times = []
	for time in stime:
		times.append(time.contents[0])
	#圖片網址
	simg = soup.select('#news_body img')
	imgs = []
	for img in simg:
		imgs.append(img.get('src'))
	
	#將爬到的資料存進資料庫
	for i in range(3):
		article = Articles.objects.create(title=titles[i], text = texts[i], detail = details[i],
				time = times[i], img = imgs[i])
		article.save()
	num = Articles.objects.all().count()
	if num >3:
		newest = Articles.objects.all().values_list("pk", flat = True)[3:6]
		Articles.objects.exclude(pk__in=list(newest)).delete()
	nba_art = Articles.objects.all()
	return render(request, 'home.html', {'nba_art':nba_art})



class ArticleView(viewsets.ModelViewSet):
	queryset = Articles.objects.all()
	serializer_class = ArticlesSerializer




