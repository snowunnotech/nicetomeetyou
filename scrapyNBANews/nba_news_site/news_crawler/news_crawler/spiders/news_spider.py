import scrapy

from datetime import datetime
from news_crawler.items import NewsCrawlerItem
from main_site.models import News

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/index',]

    def parse(self, response):
        news_url_list = response.xpath('//div[@id="news_body"]//a/@href').extract()

        for news_url in news_url_list:
            news_url = 'https://nba.udn.com' + news_url
            if not News.objects.filter(news_url=news_url).exists():
                yield scrapy.Request(news_url, callback=self.parse_news_detail_content)

    def parse_news_detail_content(self, response):
        
        news_url = response.url
        title = response.xpath('//h1/text()').extract_first()
        author = response.xpath('//div[@class="shareBar__info--author"]/text()').extract_first()
        context_list = response.xpath('//p/text()|//strong/text()').extract()
        img_url = response.xpath('//figure[@class="photo_center photo-story"]//img/@data-src').extract_first()
        post_date = response.xpath('//div[@class="shareBar__info--author"]//span/text()').extract_first()
        create_date = datetime.now()

        context = "".join(context_list)

        news = NewsCrawlerItem(
                    title=title,
                    author=author,
                    context=context,
                    news_url=news_url,
                    img_url=img_url,
                    post_date=post_date,
                    create_date=create_date
                )

        yield news