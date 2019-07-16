from bs4 import BeautifulSoup
import requests
import pymongo
import time
import random
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.test

collection = db.news


all_news = []
news = []
p = 1
for page in range(2):
    response = requests.get('https://nba.udn.com/nba/cate/6754/-1/newest/' + str(2 - page)).text
    html = BeautifulSoup(response)

    # 各文章連結
    each_num = html.select('#news_list_body a ')
    articles = []
    for n in range(len(each_num)):
        num = each_num[len(each_num) - n - 1]['href'][16:]

        response = requests.get('https://nba.udn.com/nba/story/6780/' + str(num)).text
        html = BeautifulSoup(response)
        # 發布時間
        times = html.select('div.shareBar__info--author span')
        utime = times[0].text
        # 文章標題
        each_title = html.select('#story_body_content h1')
        title = each_title[0].text
        # 新聞內容
        each_article = html.select('#story_body_content p')
        article = ''
        for i in range(1, len(each_article)):
            if each_article[i].text == '':
                continue
            else:
                article += each_article[i].text

        articles.append({'time': utime, 'title': title, 'article': article})
    for i in range(len(articles)):
        news.append(articles[i])
    print('已完成' + str(p) + '頁')
    p = p + 1
    time.sleep(random.random())

for i in range(len(news)):
    all_news.append(news[i])
# 存至mongodb
for a in range(len(all_news)):
    result = collection.insert(all_news[a])
