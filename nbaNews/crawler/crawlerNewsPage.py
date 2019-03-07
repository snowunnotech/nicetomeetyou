import requests
from bs4 import BeautifulSoup
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nbaNews.settings')
import django

django.setup()
from news.models import News


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
        unwant.extract()

        unwant = content.find('div', {'class': 'shareBar'})
        unwant.extract()

        unwant = content.find('figure', {'class': 'photo_center'})
        unwant.extract()


        news2, isCreate = News.objects.get_or_create(url=url)

        news2.content = content.text
        news2.title = title
        news2.uploadDatetime = uploadDatetime
        news2.save()

    def run(self):
        return


if __name__ == '__main__':
    # -1/newest/1
    crawler = CrawlerNewsPage('/nba/story/6780/3683507')
    # crawler.run()
