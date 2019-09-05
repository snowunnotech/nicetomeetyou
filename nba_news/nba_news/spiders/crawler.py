import scrapy
from bs4 import BeautifulSoup
from nba_news.items import NbaNewsItem

class NBA_Crawler(scrapy.Spider):
    name = 'NBA'
    start_url = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        domain = 'https://nba.udn.com'
        res = BeautifulSoup(response.body.text, 'html.parser')
        for news in res.find(id = 'news_body').find_all('a'):
            # print(domain + news.get('href'))
            yield scrapy.Request(domain + news.get('href'), self.parse_detail)

    def parse_detail(self, response):
        res = BeautifulSoup(response.body.text, 'html.parser')
        nbanewsitem = NbaNewsItem()

        title = res.find(class_='story_art_title').text
        url = res.find(property='og:url').get('content')
        date = res.find(class_='shareBar__info--author').find('span').text
        source = res.find(class_='shareBar__info--author').text.replace(date, '')
        content = ''.join(i.text for i in res.find(id='story_body_content').find_all('p'))
        content = content.replace(' Getty Imagesfacebooktwitterpinterest', '')

        nbanewsitem['title'] = title
        nbanewsitem['url'] = url
        nbanewsitem['date'] = date
        nbanewsitem['source'] = source
        nbanewsitem['content'] = content
        return nbanewsitem

