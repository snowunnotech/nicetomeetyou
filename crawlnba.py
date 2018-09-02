import requests
import urllib.request
from bs4 import BeautifulSoup


res = requests.get('https://nba.udn.com/nba/cate/6754')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
nbanews  = soup.find('div', id='news_list_body')

# print(nbanews)
# store total href
news_href = []
news_h3 = []
news_img = []
news_p = []

for a in nbanews.findAll('a'):
    news_href.append('https://nba.udn.com/'+a.get('href'))
    news_p.append(a.text)

for ig in nbanews.findAll('img'):
    news_img.append(ig['data-src'])

for h in nbanews.findAll('h3'):
    news_h3.append(h.text)



# print(news_href)
# print(news_h3)
# print(news_img)
# print(news_p)

# print(text)
# req = urllib.request.Request('https://nba.udn.com/nba/cate/6754')
# data = urllib.request.urlopen(req).read()
#
# bs = BeautifulSoup(data, 'html.parser')
#
# print(bs.find('img'))