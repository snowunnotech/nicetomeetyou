from __future__ import absolute_import
import requests
from bs4 import BeautifulSoup
from news.models import News
from celery.schedules import crontab
from celery.task import periodic_task


class Crawler():
    def __init__(self):
        self.url = 'https://nba.udn.com/nba/index?gr=www'

    def run(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        all_focus_news = soup.find('div', id='news_body').find_all('dt')
        for focus_news in all_focus_news:
            try:
                news_href = focus_news.find('a', href=True)
                news_detail = self.get_news_detail(news_href['href'])
                News.objects.get_or_create(
                    news_id=news_detail['news_id'],
                    author=news_detail['author'],
                    datetime=news_detail['datetime'],
                    title=news_detail['title'],
                    href=news_detail['href'],
                    content=news_detail['content']
                )
            except TypeError:
                # ads
                pass

    def get_news_detail(self, href):
        news_detail = dict()
        r = requests.get('https://nba.udn.com/{}'.format(href))
        soup = BeautifulSoup(r.text, 'html.parser')
        news_detail['news_id'] = r.url.split('/')[-1]
        news_detail['href'] = r.url
        news_detail['title'] = soup.find('h1', {'class': 'story_art_title'}).text
        shareBar__info = soup.find('div', {'class': 'shareBar__info--author'})
        news_detail['datetime'] = shareBar__info.find('span').text
        news_detail['author'] = shareBar__info.text.replace(news_detail['datetime'], '')
        news_detail['content'] = "\n".join(p.text for p in soup.find(id='story_body_content').find_all('p')[1:])
        return news_detail

@periodic_task(ignore_result=True, run_every=crontab(minute=30)
def period_crawler():
    print('period start')
    c = Crawler()
    c.run()