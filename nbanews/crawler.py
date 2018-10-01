from bs4 import BeautifulSoup
import requests
import sqlite3
import os
import hashlib

url = 'https://nba.udn.com/nba/index?gr=www'
html = requests.get(url)
html.encoding = "utf-8"

sp = BeautifulSoup(html.text, "html.parser")
news_body = sp.select('#news_body')
old_md5 = ''
md5 = hashlib.md5(news_body[0].text.encode('utf-8-sig')).hexdigest()
if os.path.exists('old_md5.txt'):
    with open('old_md5.txt','r') as f:
        old_md5 = f.read()
    with open('old_md5.txt','w') as f:
         f.write(md5)
else:
    with open('old_md5.txt','w') as f:
         f.write(md5)

if md5 != old_md5:
    print('資料已更新')
else:
    print('資料未更新，從資料庫讀取...')
    quit()

news_html = news_body[0].find_all("a");
news_urls = []  #網址串列
news = []       #新聞串列

for tag in news_html:
  news_urls.append('https://nba.udn.com'+tag.get("href"))

for new_url in news_urls:
    html_tmp = requests.get(new_url)
    html_tmp.encoding = "utf-8"
    sp2 = BeautifulSoup(html_tmp.text, "html.parser")
    title = sp2.select('.story_art_title')[0].string
    content_html = sp2.select('#shareBar')[0].next_sibling.next_sibling.next_sibling.next_sibling.find_all("p")
    content = ''
    for c in content_html[1:]:
        content = content + str(c)

    created_at = sp2.select(".shareBar__info--author span")[0].string
    feature_pic = sp2.find('figure').find("img").get("data-src")
    new_data = {
        "title": title,
        "content": content,
        "feature_pic": feature_pic,
        "created_at": created_at
    }
    news.append(new_data)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "db.sqlite3")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
news.reverse()
for new in news:
    check_sql = "SELECT title,created_at FROM nbanews_nbanewsmodel WHERE title='{}' AND created_at='{}'".format(new['title'],new['created_at'])
    cursor = conn.execute(check_sql)
    row = cursor.fetchone()
    if row == None:
        insert_sql = "INSERT INTO nbanews_nbanewsmodel (title,content,feature_pic,created_at) VALUES ('{}','{}','{}','{}')".format(
            new['title'], new['content'], new['feature_pic'], new['created_at'])
        cursor.execute(insert_sql)
        conn.commit()
        print("Records created successfully")
conn.close()