import scrapy
from bs4 import BeautifulSoup


class NBA_Crawler(scrapy.Spider):
    name = 'NBA'
    start_url = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        domain = 'https://nba.udn.com'
        res = BeautifulSoup(response.body.text, 'html.parser')
        for news in res.find(id = 'news_body').find_all('a'):
            print(domain + news.get('href'))
            yield scrapy.Request(domain + news.get('href'), self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body.text, 'html.parser')
        title = res.find(class_='story_art_title').text
        print(title)
