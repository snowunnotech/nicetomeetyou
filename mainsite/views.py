from django.shortcuts import render
from django.http import HttpResponse
from .models import news_record
from datetime import datetime
from rest_framework import viewsets, filters
from .serializers import news_recordSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
import requests
from bs4 import BeautifulSoup
import sqlite3
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("DROP TABLE mainsite_news_record")
cmd = 'CREATE TABLE IF NOT EXISTS mainsite_news_record ' \
        '(id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
        'title TEXT, article TEXT)'
cursor.execute(cmd)
# cursor.execute("DELETE FROM mainsite_news_record")
url = requests.get("https://nba.udn.com/nba/index?gr=www")
url.encoding = 'utf-8'
sp = BeautifulSoup(url.text, 'html.parser')
# print(sp.prettify())  # 打印出結構化的資料
links = sp.find_all('a')  # find hot news links
for link in links:
    href = link.get('href')
    if href != None and href.startswith('/nba/story/6780/'):
        # print("https://nba.udn.com/"+href)
        url = requests.get("https://nba.udn.com/"+href)
        url.encoding = 'utf-8'
        sp = BeautifulSoup(url.text, 'html.parser')
        t = sp.h1.text  # find hot news title
        sp2 = sp.find_all('p')  # find hot news article
        # print(sp2.text)
        ar = []
        a = ''
        for sp3 in sp2:
            ar.append(sp3.text.replace(" ", "").replace("'", "`"))
        del ar[0]
        a = a.join(ar)  # 合併多個字串為一個字串

        cursor.execute("insert into mainsite_news_record(title, article) values ('%s', '%s')" % (t, a))

conn.commit()
conn.close()


def news_index(request, id):
    p = news_record.objects.get(id=id)
    now = datetime.now()
    return render(request, 'article.html', locals())

def homepage(request):
    news = news_record.objects.all()
    row = len(news)  # 總資料數
    # for i in row:
    #     news1 = news[i].article
    news1 = news[1].article
    time = datetime.now()
    return render(request, 'homepage.html', locals())


class news_recordViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
        """
    queryset = news_record.objects.all()
    serializer_class = news_recordSerializer



