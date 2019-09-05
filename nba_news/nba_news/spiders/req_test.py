import requests
from bs4 import BeautifulSoup

url = 'https://nba.udn.com/nba/index?gr=www'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
domain = 'https://nba.udn.com'

for news in soup.find(id = 'news_body').find_all('a'):
    print(domain + news.get('href'))
    news_content = requests.get(domain + news.get('href'))
    news_soup = BeautifulSoup(news_content.text, 'html.parser')
    print(news_soup.find(class_='story_art_title').text)

