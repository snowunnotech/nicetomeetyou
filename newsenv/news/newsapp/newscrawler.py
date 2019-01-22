import requests
from bs4 import BeautifulSoup
import urllib
import re
import html
from django.shortcuts import render, redirect
from .models import News
import json
import time

def crawler(request):
    link = 'https://nba.udn.com/nba/index?gr=www'
    news_crawler(link)
    return redirect('newsapi')

def news_crawler(link):
    url = link #選擇網址
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15' #偽裝使用者
    headers = {'User-Agent':user_agent}
    data_res = urllib.request.Request(url=url,headers=headers)
    data = urllib.request.urlopen(data_res, timeout=20)
    sp = BeautifulSoup(data, "html.parser")
    #標題
    title=[]
    titles = sp.find("div",{"id":"news"}).findAll("h3")
    for i in titles:
        title.append(i.text)
    link=[]
    links = sp.find("div",{"id":"news"}).findAll("a", href = re.compile('/nba/story/'))
    for i in links:
        link.append('https://nba.udn.com/'+i['href'])
    for news_title, news_link in zip(title,link):
        content_crawler(news_title,news_link)
def content_crawler(news_title,news_link):
    url = news_link #選擇網址
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15' #偽裝使用者
    headers = {'User-Agent':user_agent}
    data_res = urllib.request.Request(url=url,headers=headers)
    data = urllib.request.urlopen(data_res, timeout=20)
    sp = BeautifulSoup(data, "html.parser")
    #標題
    content_list= []
    content = sp.find("div",{"id":"story_body_content"}).findAll("span")
    news_time = content[0].text
    for i in content:
        content_list.append(i)
    content_group = content_list[2].text
    content_group = content_group.lstrip(' NBAfacebooktwitterpinterest')
    content_group = content_group.lstrip(' 美聯社facebooktwitterpinterest')
    content_one,another =  content_group.split('.inline-ad { position')
    nothing,content_two =  another.split('); });')
    news_content = content_one+content_two
    print(news_content)
    photo = sp.find("figure",{"class":"photo_center photo-story"}).find('img')['data-src']
    news_img = photo
    sql(news_title,news_link,news_time,news_content,news_img)

def sql(news_title,news_link,news_time,news_content,news_img):

        
    try:
        newsdb = Blog.objects.get(news_title=news_title)
        newsdb.news_link = news_link
        newsdb.news_time = news_time
        newsdb.news_content= news_content
        newsdb.news_img = news_img


        newsdb.save()
        print('更新資料')
    except:
        newsdb = News.objects.create(news_title=news_title,news_link=news_link, news_time=news_time, news_content=news_content, news_img=news_img)
        newsdb.save()
        print('成功存入一筆資料')
