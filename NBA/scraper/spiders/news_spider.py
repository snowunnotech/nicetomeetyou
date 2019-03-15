import scrapy
from bs4 import BeautifulSoup
from datetime import datetime
from scraper.items import NBANewsItem

class NewsInFocusSpider(scrapy.Spider):
    name = 'news_in_focus'
    start_urls = [
        'https://nba.udn.com/nba/index?gr=www',
    ]

    def parse(self, response):
        news_body = response.css('div#news_body')

        for href in news_body.css('a::attr(href)'):
            yield response.follow(href, callback=self.parse_news)

    def parse_news(self, response):

        
        html = response.body
        soup = BeautifulSoup(html, 'lxml')

        item = NBANewsItem()
        item['url'] = response.url
        item['title'] = soup.select('#story_body_content > h1')[0].text
        
        published = soup.select('#shareBar > div.shareBar__info > div > span')[0].text
        item['published'] = datetime.strptime(published, '%Y-%m-%d %H:%M')

        news_text = ''
        for p in soup.select('#story_body_content > span > p'):
            news_text += p.text
        item['text'] = news_text

        item['img_url'] = soup.select('#story_body_content figure img ')[0]['data-src']

        yield item
