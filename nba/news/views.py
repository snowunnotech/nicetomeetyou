# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from news.craw import newscraw
from news.models import News

# Create your views here.
def index(request):
	datas = newscraw()
	for data in datas:
		title , content , link = data["title"] , data["content"] , data["link"]
		if len(News.objects.filter(title= title))==0:
			newNews = News(title = title, content = content, link = link)
			newNews.save()
			print "SAVE"
	return render(request,'index.html')