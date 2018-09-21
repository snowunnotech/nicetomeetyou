from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from selenium import webdriver
from bs4 import BeautifulSoup
from .models import Post

import requests
from datetime import datetime
# Create your views here.

def parse():
    rq = requests.get('https://nba.udn.com/nba/cate/6754')
    soup = BeautifulSoup(rq.text, "html.parser")

    new_posts = []
    history_id_list = [history.pid for history in Post.objects.all()]

    for post in soup.select('#news_list_body dt a'):
        
        pid   = int(post.get('href')[-7:])

        if pid in history_id_list:
            continue

        title = post.select('h3')[0].string
        image = post.select('img')[0]['data-src']
        url   = 'https://nba.udn.com' + post['href']

        rq = requests.get(url)
        content_soup = BeautifulSoup(rq.text, "html.parser")
        date  = content_soup.select('.shareBar__info--author span')[0].string
        print(date)
        date  = datetime.strptime(date, '%Y-%m-%d %H:%M')
        print(date)
        content = ""
        for c in content_soup.select('#story_body_content p'):
            content += str(c)

        new_posts.append({
            'title': title, 'id': pid, 'image': image, 
            'url': url, 'date': date, 'content': content
        })
        
    if len(new_posts):
        for post in new_posts:
            new_post = Post(
                pid = post['id'], post_title = post['title'],
                post_image_url = post['image'], post_url = post['url'],
                post_date = post['date'], post_content = post['content']
            )
            new_post.save()