import requests
from bs4 import BeautifulSoup
import sqlite3
import psycopg2

# conn = sqlite3.connect('db.sqlite3')
conn = psycopg2.connect(database="d8jgfcpejnfh3q", user="fsqwfsuloagkhe", password="fbfe9ff659a90bc257818681eeecde2d30005c5d98425b26045dfff69cdeb39a", host="ec2-50-19-222-129.compute-1.amazonaws.com", port="5432")
c = conn.cursor()

url = 'https://nba.udn.com/nba/index?gr=www'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
domain = 'https://nba.udn.com'

for news in soup.find(id = 'news_body').find_all('a'):
    # print(domain + news.get('href'))
    news_content = requests.get(domain + news.get('href'))
    news_soup = BeautifulSoup(news_content.text, 'html.parser')

    title = news_soup.find(class_='story_art_title').text
    story_url = news_soup.find(property = 'og:url').get('content')
    date = news_soup.find(class_='shareBar__info--author').find('span').text
    source = news_soup.find(class_='shareBar__info--author').text.replace(date, '')
    content = ''.join(i.text for i in news_soup.find(id = 'story_body_content').find_all('p'))
    content = content.replace(' Getty Imagesfacebooktwitterpinterest', '')
    information = [title, story_url, date, source, content]

    #檢查是否已經爬過
    # c.execute('select url from nba_news where url = ?', (story_url,))
    c.execute('select url from nba_news where url = %s', (story_url,))
    row = c.fetchall()
    if len(row) == 0:
        # c.execute('insert into nba_news(title, url, date, source, content) values(?, ?, ?, ?, ?)', information)
        c.execute('insert into nba_news(title, url, date, source, content) values(%s, %s, %s, %s, %s)', information)
        conn.commit()

