from bs4 import BeautifulSoup
from .models import NBANewsPage

import requests

class crawler(object):
    def __init__(self):
        self.header = { "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36" }
        self.base_url = "https://nba.udn.com"
        self.home = "/nba/index?gr=www"
        self.title = list()
        self.href = list()
        self.content = list()

    def getData(self):
        try:
            url = self.base_url + self.home
            r = requests.get(url, headers = self.header)
            soup = BeautifulSoup(r.text, features = 'lxml')

            news_body = soup.find("div", {"class" : "box_body"})
            for dt in news_body.find_all("dt", limit = 3):
                # 取得標題
                self.title.append(dt.h3.text)

                # 取得連結
                self.href.append(dt.a.get("href"))

                # 取得新聞詳情
                r = requests.get(self.base_url + dt.a.get("href"), headers = self.header)
                soup = BeautifulSoup(r.text, features = 'lxml')
                content = soup.find("div", {"id" : "story_body_content"}).find_all("span")[2]
                self.content.append(content)

        except Exception as e:
            print(e)

    def saveData(self):
        try:
            for (x, y, z) in zip(self.title, self.href, self.content):
                new_data = NBANewsPage()
                if NBANewsPage.objects.filter(href = self.base_url + y):
                    print("skipData")
                    break
                else:
                    print("saveData")
                    new_data.title = x
                    new_data.href = self.base_url + y
                    new_data.content = str(z)
                    # new_data = NBANewsPage.objects.create(title = x, href = self.base_url + y, content = str(z))
                    new_data.save()
        except Exception as e:
            print(e)

crawler = crawler()
crawler.getData()
crawler.saveData()