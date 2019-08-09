import scrapy
from bs4 import BeautifulSoup
from nbatest.items import NbatestItem

class NbaCrawler(scrapy.Spider):
    name = 'nba'
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        domain = 'https://nba.udn.com'

        res = BeautifulSoup(response.body)
        for news in res.select('#news_body dt'):
            if news.select('h3'):
                sub_url = domain + news.select('a')[0]['href']
                yield scrapy.Request(sub_url, self.parse_detail)

    def parse_detail(self, response):

        res = BeautifulSoup(response.body)
        item = NbatestItem()
        item['title'] = res.select('#story_body_content > h1')[0].text
        item['post_datetime'] = res.select('#shareBar > div.shareBar__info > div > span')[0].text
        item['image_url'] = res.select('#story_body_content > span > p > figure > a > img')[0]['data-src']

        contents = res.select('#story_body_content > span > p, div.video-container')[1:]
        content_str = ""
        for content in contents:
            content_str = content_str + str(content)

        item['content'] = content_str

        sub_id = res.select('#story_body')[0]['data-sub']
        article_id = res.select('#story_body')[0]['data-article']
        uid = sub_id + '/' + article_id
        item['uid'] = uid

        return item