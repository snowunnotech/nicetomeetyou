import re
import requests
from bs4 import BeautifulSoup

host = 'https://nba.udn.com'
url = '/nba/index?gr=www'

res = requests.get(host+url)

soup = BeautifulSoup(res.content, 'html.parser')

news_body = soup.find(id='news_body')
news = news_body.find_all('a')
for n in news:
    news_url = host+str(n.get('href'))
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