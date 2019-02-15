import requests
import json
from django.conf import settings
from bs4 import BeautifulSoup
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_crawler.settings')
django.setup()
from crawler.models import News
# news_id = models.IntegerField(primary_key=True)
# title = models.CharField(max_length=40)
# author = models.CharField(max_length=25)
# datePublished = models.DateTimeField()
# image = models.URLField()
# context = models.TextField()

def get_webdata(url):
    response = requests.get(url)
    if response.raise_for_status():
        return response.raise_for_status()        
    else:        
        return response.text

def get_news_links(url, tag):
    urls = []
    sp = BeautifulSoup(get_webdata(url), 'html.parser')
    datas = sp.select(tag)
    for data in datas:
        urls.insert(0,data['href'])
    return urls

def get_news_detail(url):
    sp = BeautifulSoup(get_webdata(url), 'html.parser')

    news = {}

    news_detail = sp.find(type='application/ld+json').text
    news_detail = json.loads(news_detail)
    news['headline'] = news_detail['headline']
    news['datePublished'] = news_detail['datePublished']
    news['author'] = news_detail['author']['name']
    news['image'] = news_detail['image']['url']
    news['content'] = ''    
    news_content = sp.select('div#story_body_content span p')
    for content in news_content:
        news['content'] = news['content'] + content.text + '<br>'
    return news

def main():
    url = 'https://nba.udn.com/nba/index'
    news_in_focus_tag = "div#news_body a"
    urls = get_news_links(url, news_in_focus_tag)
    for news_url in urls:        
        news = get_news_detail('https://nba.udn.com/'+news_url)
        if News.objects.filter(title=news['headline']):
            pass
        else:
            News.objects.create(title=news['headline'], author=news['author'], datePublished=news['datePublished'],
            image=news['image'], context=news['content'])

if __name__ == '__main__':
    main()
    
    
