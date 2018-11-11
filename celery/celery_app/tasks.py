from __future__ import absolute_import, unicode_literals
from celery import shared_task, chain, uuid
from celery_app import app
from bs4 import BeautifulSoup
import requests
import json


@app.task
def chain_crawler():
    server_ip = "35.185.173.110"
    chain(get_mainweb.s(), process.s(server_ip))()


@app.task
def get_mainweb():
    url = "https://nba.udn.com/nba/index?gr=www"
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, "lxml")
    urls = list()
    for s in soup.select("div[id='news_body'] a"):
        urls.append(s['href'])
    return urls


@app.task
def etl_news_detail(pattern):
    url = "https://nba.udn.com" + pattern
    res = requests.get(url=url)
    news = dict()
    soup = BeautifulSoup(res.text, "lxml")
    s = soup.find("script", type='application/ld+json')
    info = json.loads(s.text)
    news['headline'] = info['headline']
    news['image'] = info['thumbnailUrl']
    news['keywords'] = info['keywords']
    news['story_id'] = float('.'.join(info['url'].split('/')[-2:]))
    news['datePublished'] = info['datePublished']
    news['dateModified'] = info['dateModified']
    news['author'] = info['author']['name']
    news['publisher'] = info['publisher']['name']
    news['logo'] = info['publisher']['logo']['url']
    news['context'] = ''
    for s in soup.select("div[id='story_body_content'] span p"):
        line = s.text
        if len(line) > 0:
            news['context'] += line
    return news


@app.task
def store_news(news, server_ip):
    url_news = "http://{}/api/news/".format(server_ip)
    res = requests.post(url=url_news, data=news)
    if res.status_code == 201:
        print('Success: id={}'.format(news['story_id']))
    else:
        print('Error: status_code={}, id={}'.format(res.status_code, news['story_id']))


@app.task(ignore_result=True)
def process(urls, server_ip):
    for pattern in urls:
        news = etl_news_detail(pattern)
        store_news(news, server_ip)


