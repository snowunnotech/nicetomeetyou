import scrapy
import requests
import time

'''
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://nba.udn.com/nba/index?gr=www',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
'''
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://nba.udn.com/nba/index?gr=www',
    ]

    def parse(self, response):
        for title, url in zip(response.xpath('//*[@id="news_body"]/dl/dt/a/h3/text()'), response.xpath('//*[@id="news_body"]/dl/dt/a//@href')):
            get_title = title.get()
            get_url = 'https://nba.udn.com' + url.get()
            get_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            
            yield {
                'title': get_title,
                'url': get_url,
                'time': time,
            }
            my_data = {'title': get_title, 'url': get_url, 'time': get_time}
            r = requests.post('http://127.0.0.1:8000/api/news/', data = my_data)
