import requests
from bs4 import BeautifulSoup
import os

from crawler.pushNotify import PushNotify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nbaNews.settings')
import django

django.setup()
from news.models import News, PushToken


class CrawlerNewsPage:
    def __init__(self, url):
        host = 'https://nba.udn.com{}'
        url = host.format(url)

        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        content = soup.select('div#story_body_content')[0]

        title = content.select('h1.story_art_title')[0].text

        uploadDatetime = content.select('div.shareBar__info--author')[0]
        uploadDatetime = uploadDatetime.select('span')[0].text

        # remove
        for c in content(["script", "style"]):
            c.decompose()

        unwant = content.find('h1', {'class': 'story_art_title'})
        try:
            unwant.extract()
        except:
            pass
        unwant = content.find('div', {'class': 'shareBar'})
        try:
            unwant.extract()
        except:
            pass

        unwant = content.find('figure', {'class': 'photo_center'})
        try:
            unwant.extract()
        except:
            pass


        news, isCreate = News.objects.get_or_create(url=url)
        if isCreate:
            self.push()
        news.content = content.text
        news.title = title
        news.uploadDatetime = uploadDatetime
        news.save()

    def push(self):
        pushTokens = PushToken.objects.all()
        for pushToken in pushTokens:
            PushNotify(pushToken.token)



if __name__ == '__main__':
    # -1/newest/1
    crawler = CrawlerNewsPage('/nba/story/6780/3683507')
    # crawler.run()
