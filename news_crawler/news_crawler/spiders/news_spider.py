import scrapy
from scrapy.utils.markup import remove_tags
from news_crawler.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'

    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        prefix = 'https://nba.udn.com'

        for news in response.css('div#news_body a::attr(href)').getall():
            self.log(prefix + news)
            yield response.follow(prefix + news, callback=self.get_content)

    def get_content(self, response):
        item = NewsItem()

        title = response.css('h1::text').get()
        pub_time = response.css('div.shareBar__info--author span::text').get()
        content = response.css('p').getall()[1:]

        item['title'] = title
        item['pub_time'] = pub_time
        item['content'] = remove_tags(''.join(content))

        yield item
