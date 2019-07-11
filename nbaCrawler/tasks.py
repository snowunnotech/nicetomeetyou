from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from selenium import webdriver
from bs4 import BeautifulSoup
from .models import Post

import re
import requests
from datetime import datetime
# Create your views here.

def parse():
    rq = requests.get('https://nba.udn.com/nba/cate/6754')
    soup = BeautifulSoup(rq.text, "html.parser")

    new_posts = []
    history_id_list = [history.pid for history in Post.objects.all()]

    for post in soup.select('#news_list_body dt a'):
        
        try:
            pid = int(post.get('href')[-7:])
        except Exception as e:
            print(f"Error Msg: {e}")
            continue

        if pid in history_id_list:
            continue

        title = post.select('h3')[0].string
        image = re.split('&', post.select('img')[0]['data-src'])[0]
        url   = 'https://nba.udn.com' + post['href']

        rq = requests.get(url)
        content_soup = BeautifulSoup(rq.text, "html.parser")
        date  = content_soup.select('.shareBar__info--author span')[0].string
        date  = datetime.strptime(date, '%Y-%m-%d %H:%M')
        content = ""
        for idx, c in enumerate(content_soup.select('#story_body_content span p')):
            if idx:
                content += str(c)
        if 'autoplay=1&' in content:
            content = content[:content.index('autoplay=1&')] + content[content.index('autoplay=1&') + 11:]

        new_posts.append({
            'title': title, 'id': pid, 'image': image, 
            'url': url, 'date': date, 'content': content
        })
        
    for post in new_posts:
        new_post = Post(
            pid = post['id'], post_title = post['title'],
            post_image_url = post['image'], post_url = post['url'],
            post_date = post['date'], post_content = post['content']
        )
        new_post.save()
