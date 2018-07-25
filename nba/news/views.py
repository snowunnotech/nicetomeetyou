# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from news.craw import newscraw
from news.models import News

# Create your views here.
def index(request):
	datas = newscraw()
	newsAdded = False
	for data in datas:
		title , content , link ,fulltext= data["title"] , data["content"] , data["link"] , data["fulltext"]
		if len(News.objects.filter(title= title))==0:
			newNews = News(title = title, content = content, link = link,fulltext = fulltext)
			newNews.save()
			newsAdded = True
	return render(request,'index.html',{"added":newsAdded})

def newspage(request):
	return render(request,'newspage.html')