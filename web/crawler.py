import requests
import sys
from bs4 import BeautifulSoup
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Date, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

Base = declarative_base()
DBSession = scoped_session(sessionmaker())
engine = create_engine('sqlite:///db.sqlite3', echo=False)
DBSession.remove()
DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)

class Article(Base):
    __tablename__ = "article_article"
    id = Column(Integer, primary_key=True)
    title = Column('title', String(50))
    author = Column('author', String(50))
    date = Column('date', Date())
    content = Column('content', Text())

    def __init__(self, title, author, date, content):
        self.title = title
        self.author = author
        self.date = date
        self.content = content

base_url = "https://nba.udn.com"
r = requests.get(base_url + "/nba/index?gr=www")
soup = BeautifulSoup(r.text, 'html.parser')
news_body = soup.find('div', id='news_body')
# print(result.text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

news_url = []
for dt in news_body.find_all('dt'):
    a = dt.find('a')
    news_url.append(a['href'])

for url in news_url:
    r = requests.get(base_url + url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('h1', {"class":'story_art_title'})
    title = title.text
    date_author = soup.find('div', {"class":'shareBar__info--author'})
    date = date_author.find('span').text
    author = date_author.contents[1]
    content = soup.find('div', id="story_body_content")
    para = []
    for p in content.find_all('p'):
        if p.find('figure'):
            continue
        para.append(p.get_text())
    content = "".join(para)
  
    date = datetime.strptime(date, '%Y-%m-%d %H:%M')
    # print(title)
    print(date)
    # print(author)
    # print(content)

    article = Article(title, author, date, content)
    DBSession.add(article)
    DBSession.commit()


# print(base_url + news_url[0])
# r = requests.get(base_url + news_url[0])
# soup = BeautifulSoup(r.text, 'html.parser')
# title = soup.find('h1', {"class":'story_art_title'})
# title = title.text
# date_author = soup.find('div', {"class":'shareBar__info--author'})
# date = date_author.find('span').text
# author = date_author.contents[1]
# content = soup.find('div', id="story_body_content")
# para = []
# for p in content.find_all('p'):
#     if p.find('figure'):
#         continue
#     para.append(p.get_text())

# print("".join(para))