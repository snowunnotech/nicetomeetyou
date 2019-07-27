import re
import requests
from bs4 import BeautifulSoup

from .models import News

host = 'https://nba.udn.com'
url = '/nba/index?gr=www'

def crawler():
    res = requests.get(host+url)

    soup = BeautifulSoup(res.content, 'html.parser')

    news_body = soup.find(id='news_body').find_all('a')
    for n in news_body:
        news_url = host+str(n.get('href'))
        if News.objects.filter(url=news_url).exists():
            return
        else:
            pass
        news_photo_url = re.match(r'^https:\/\/pgw\.udn\.com\.tw\/gw\/photo\.php\?u=(.+)&x=.+$', str(n.find('img').get('src'))).group(1)
        news_title = n.find('h3').text
        news_top = n.find('p').text
        res = requests.get(host+str(n.get('href')))
        soup = BeautifulSoup(res.content, 'html.parser')
        story_body = soup.find(id='story_body_content')
        story = story_body.find_all('span')[2]
        p = story.find_all('p')[1:]
        content = ""
        p = [x for x in p if x.text]
        for x in p:
            content += x.text + '\n'
        news_content = content

        print(news_title)
        print(news_url)
        print(news_top)
        print(news_photo_url)
        print(news_content)

        model = News(title=news_title, url=news_url, top=news_top, photo_url=news_photo_url, content=news_content)
        model.save()
