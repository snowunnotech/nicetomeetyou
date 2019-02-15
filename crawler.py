import urllib.request
import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = 'https://nba.udn.com/nba/index?gr=www'
urlGet = requests.get(url)
fp = urllib.request.urlopen(urlGet.url)
soup = BeautifulSoup(fp , 'html.parser')
news_raw = soup.find_all(id='news')[0]
news = []

for a in news_raw.find_all('a'):
    story = a['href']
    if 'story' in story:
        news.append('https://nba.udn.com' + story)

print(news)
