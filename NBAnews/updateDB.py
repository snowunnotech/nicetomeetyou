# -*- encoding: utf8 -*-

import os
import sys

from django.conf import settings
import django.utils.timezone as timezone
import django
import requests
from bs4 import BeautifulSoup as BS

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NBAnews.settings")
django.setup()

from news.models import News

class Spider():
    def __init__(self):
        self.home = 'https://nba.udn.com/nba/index?gr=www'

    def getPage(self, url):
        req = requests.get(url)
        req.encoding = 'utf8'
        data = req.text
        soup = BS(data, 'html.parser')

        return soup

    def getNewsID(self, url):
        soup = self.getPage(url)
        news = soup.findAll('dt')
        news = soup.findAll('div', {'id':'news_list_body'})[0].findAll('dt')

        return [n.a['href'] for n in news]

    def getNewsData(self, news_id):
        url = 'https://nba.udn.com' + news_id
        soup = self.getPage(url)

        news = {}
        
        date = soup.findAll('div', {'class':'shareBar__info--author'})[0].findAll('span')[0].text

        title = soup.findAll('h1', {'class':'story_art_title'})[0].text

        content = soup.findAll('div', {'id':'story_body_content'})[0].findAll('span')[2].findAll('p')[1].text

        news['news_id'] = int(news_id.split('/')[-1])
        news['title'] = title
        news['date'] = date
        news['content'] = content

        return news

    def run(self):
        soup = self.getPage(self.home)

        url = 'https://nba.udn.com' + soup.findAll('a', {'class': 'more'})[0]['href']

        for page in range(10):
            page_url = url + '/-1/newest/%d' % (page)
            news_ids = self.getNewsID(page_url)

            for news_id in news_ids:
                new = self.getNewsData(news_id)
                try:
                    n = News.objects.get(news_id=new['news_id'])
                    return 
                except Exception as e:
                    News.objects.create(news_id=new['news_id'], title=new['title'], content=new['content'], date=new['date'])

        

if __name__ == '__main__':

    spider = Spider()
    spider.run()

    #for new in News.objects.order_by('-date'):
    #    print(new.title + '\t' + str(new.date))
