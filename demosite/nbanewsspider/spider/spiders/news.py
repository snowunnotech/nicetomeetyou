
import scrapy

from spider.items import NewsItem
from spider.postgres_provider import PostgresProvider
from spider.settings import DATABASES


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/cate/6754/-1/newest']

    def __init__(self, *args, **kwargs):
        super(NewsSpider, self).__init__(*args, **kwargs)
        self.postgres_provider = PostgresProvider()
        self.postgres_provider.connect(
            DATABASES['default']['USER'],
            DATABASES['default']['PASSWORD'],
            DATABASES['default']['NAME'])
        self.get_news_list()

    def get_news_list(self):
        news = self.postgres_provider.meta.tables['nbanewsreader_news'] 
        self.news_uid = [row[0] for row in self.postgres_provider.connection.execute(news.select())] 

    def parse(self, response):
        last_href = response.css(
            'div.pagelink gonext a[data-id="last"]::attr(href)').extract_first()
        last_page = int(last_href[last_href.rfind('/') + 1:])

        #for i in range(1, last_page+1):
        for i in range(1, 20):
            url = 'https://nba.udn.com/nba/cate/6754/-1/newest/' + str(i)
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        post_list = response.css('div#news_list_body dl dt')
        for post in post_list:
            try:
                href = post.css("a::attr(href)").extract_first()
                uid = href[href.rfind('/') + 1:]

                if uid in self.news_uid:
                    continue

                url = 'https://nba.udn.com' + href
                yield scrapy.Request(url, callback=self.parse_article)
            except IndexError:
                pass

    def parse_article(self, response):
        item = NewsItem()
        target = response.css('div#story')
        item['uid'] = response.css(
            'div#story_body::attr(data-article)').extract_first()
        item['url'] = response.url
        item['title'] = target.css('h1.story_art_title::text').extract_first()
        item['author'] = target.css(
            'div.shareBar__info--author::text').extract_first()
        item['published_at'] = target.css(
            'div.shareBar__info--author span::text').extract_first()

        content = [p.extract() for p in target.css(
            'div#story_body_content span p::text, div#story_body_content span p a strong::text')]
        item['content'] = ''.join(content)

        yield item
