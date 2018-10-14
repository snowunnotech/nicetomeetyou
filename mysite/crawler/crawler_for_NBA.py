from bs4 import BeautifulSoup
import sqlite3
import requests

conn = sqlite3.connect('D:\Django\\nicetomeetyou\mysite\db.sqlite3')
urls = conn.execute('select url from NBANews_news').fetchall()
html = requests.get('https://nba.udn.com/nba/index?gr=www').text
sp = BeautifulSoup(html, 'html.parser')
data = sp.find_all('div', {'class' : 'box_body'})[0].find_all('a')
for d in data:
    url = d.get('href')
    title = d.find('h3').text
    subtitle = d.find('p').text
    try:
        conn.execute("insert into NBANews_news values('{}', '{}', '{}')".format(title, subtitle, url))
        urls.append(url)
        conn.commit()
    except:
        pass
