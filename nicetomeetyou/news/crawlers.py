from datetime import  datetime
import requests as rs
from bs4 import BeautifulSoup as bs

from . models import News


def string_to_datetime(string):
    return datetime.strptime(string, "%Y-%m-%d %H:%M")


class Crawler:

    domain = "https://nba.udn.com"
    first_page = domain + "/nba/index?gr=www"

    def parse_news_urls(self, soup):
        news_body = soup.select('#news_body')[0].find_all('dt')
        news_href = list()
        for i in news_body:
            try:
                news_href.append(self.domain + i.a['href'])
            except TypeError as e:
                print(e)
                pass
        return news_href

    @staticmethod
    def parse_number(url):
        number = url.split("/")[-1]
        return int(number)

    @staticmethod
    def parse_title(soup):
        title = soup.find("h1", class_="story_art_title").text
        return title

    @staticmethod
    def parse_published_date(soup):
        published_date = soup.find("div", class_="shareBar__info--author").find("span").text
        return published_date

    @staticmethod
    def parse_image(soup):
        image = soup.find("a", class_="grouped-photo").find("img")['data-src']
        return image

    @staticmethod
    def parse_contents(soup):
        paragraph = soup.find(id="story_body_content").find_all("p")
        contents = ""
        for p in paragraph:
            if p.text is not "":
                contents += p.text + "\n"
        return contents

    def parse_news_information(self, url):

        res = rs.get(url)
        soup = bs(res.text, "html5lib")

        number = self.parse_number(url)
        title = self.parse_title(soup)
        image = self.parse_image(soup)
        contents = self.parse_contents(soup)
        published_date = string_to_datetime(self.parse_published_date(soup))

        news = News.create(number, title, image, contents, published_date)
        news.save()

    def run(self):

        res = rs.get(self.first_page)
        soup = bs(res.text, "html5lib")

        news_urls = self.parse_news_urls(soup)
        for url in news_urls:
            self.parse_news_information(url)
