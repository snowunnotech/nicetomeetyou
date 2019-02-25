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
token = open('./token.txt', 'r').read().strip()

for news in news_raw.find_all('dt'):
    try:
        title = news.find_all('h3')[0].string
        news_url = news.find_all('a')[0]['href']
        if 'story' in news_url:
            data.append((title, 'https://nba.udn.com' + news_url))
    except:
        pass

for ele in data:
    r = requests.post('http://illinois.cs.nccu.edu.tw:8000/api/news/', data={ 'title':ele[0], 'link':ele[1] }, headers={'Authorization': token})
    print(r.text)
