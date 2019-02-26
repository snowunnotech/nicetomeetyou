import urllib.request
import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = 'https://nba.udn.com/nba/index?gr=www'
urlGet = requests.get(url)
fp = urllib.request.urlopen(urlGet.url)
soup = BeautifulSoup(fp , 'html.parser')
news_raw = soup.find_all(id='news')[0]
data = []
token = open('/home/vodo/nicetomeetyou/token.txt', 'r').read().strip()

for news in news_raw.find_all('dt'):
    try:
        title = news.find_all('h3')[0].string
        link = news.find_all('a')[0]['href']
        pic_link = news.find_all('img')[0]['src'].split('&')[0]
        if 'story' in link:
            data = { 'title': title, 'link' : 'https://nba.udn.com' + link, 'pic_link' : pic_link}
            r = requests.post('http://illinois.cs.nccu.edu.tw:8000/api/news/', data=data, headers={'Authorization': token})
            print(r.text)
    except:
        pass

