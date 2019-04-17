import sqlite3
import urllib.request as req
from functools import reduce

import requests
# import scrapy
from bs4 import BeautifulSoup
url =  ' https://nba.udn.com/nba/index?gr=www'
domain = 'https://nba.udn.com'

sql = "insert into new_new(article,title,detail) values (?,?,?)"
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor();

with req.urlopen(url) as respone:
    origin = respone.read().decode("utf-8")
    soup = BeautifulSoup(origin,'html.parser')
    newList = soup.select("div #news_body dt")
    urlList = []

    for ele in newList[:-1]:
        urlList.append(domain+ele.select('a')[0]['href'])
    data = []
    for url in urlList:
        soup1 = BeautifulSoup(requests.get(url).text,'html.parser')
        article = soup1.find("div",id="story_body")["data-article"]

        titles = soup1.select(".story_art_title")[0].text
    #soup1.select("div #story_body_content span p")[1:]
        temp = [ x.text for x in soup1.select("div #story_body_content span p")[1:] ]
        details="".join(temp)

        print(article,titles,details)
        cur.execute(sql,(article,titles,details))
conn.commit()
conn.close()
