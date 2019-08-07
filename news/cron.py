from news.models import News
import requests
from bs4 import BeautifulSoup


nbaUrl = 'https://nba.udn.com'


def get_or_create_in_news_table(news_array):
    for news in news_array:
        News.objects.update_or_create(
            title=news.title,
            defaults={
                'title': news.title,
                'imgUrl': news.imgUrl,
                'time': news.time,
                'url': news.url,
                'payload': news.payload
            }
        )


def news_spider():
    res = requests.get('https://nba.udn.com/nba/index?gr=www')
    soup = BeautifulSoup(res.text, 'html.parser')

    news = soup.find('div', id='news')
    array = news.find_all('dt')

    results = []
    for element in array:
        if element.find('style'):
            break
        results.append(soupNews(element))
    get_or_create_in_news_table(results)
    print('cron job hi')
    return results


class New:
    def __init__(self, title, imgUrl, time, payload, url):
        self.title = title
        self.imgUrl = imgUrl
        self.time = time
        self.payload = payload
        self.url = url


def soupNews(element):
    return New(
        title=element.find('h3').string,
        imgUrl=element.find('img').get('src'),
        time=element.find('b').string,
        payload=element.find('p').string,
        url=nbaUrl + element.find('a').get('href')
    )
