import sqlite3
import urllib.request as req
from functools import reduce

import requests
# import scrapy
from bs4 import BeautifulSoup



sql = "insert into new_new(article,title,detail) values (?,?,?)"
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor();
def find_exist_data(existData):

    selectSql = "select article from new_new";
    for i in cur.execute(selectSql):
        existData.append(i[0]);
def crawler_nba(existData,url,domain):
    with req.urlopen(url) as respone:
        origin = respone.read().decode("utf-8")
        soup = BeautifulSoup(origin,'html.parser')
        newList = soup.select("div #news_body dt")
    urlList = []
    for ele in newList[:-1]:
        urlList.append(domain+ele.select('a')[0]['href'])

    for url in urlList:
        soup1 = BeautifulSoup(requests.get(url).text,'html.parser')
        article = soup1.find("div",id="story_body")["data-article"]

        titles = soup1.select(".story_art_title")[0].text
        if article not in existData :
            temp = [ x.text for x in soup1.select("div #story_body_content span p")[1:] ]
            details="".join(temp)

            print(article,titles,details)
            insert_data(sql,article,titles,details)

def insert_data(sql,article,titles,details):

    cur.execute(sql, (article, titles, details))

def main():
    url = ' https://nba.udn.com/nba/index?gr=www'
    existData = []
    domain = 'https://nba.udn.com'
    find_exist_data(existData)
    crawler_nba(existData,url,domain)
    conn.commit()
    conn.close()
if __name__=="__main__":
	main();