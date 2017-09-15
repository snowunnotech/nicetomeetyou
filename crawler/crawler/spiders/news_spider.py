# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import datetime
import pytz

from scrapy import Selector, Request
from scrapy.spiders import BaseSpider

from crawler.items import CrawlerItem

class NewsSpider(BaseSpider):
    name = "news_spider"
    allowed_domains = ["nba.udn.com"]
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        # only need the links in <div id="news_body">
        news_body = response.xpath('//div[@id="news_body"]').extract()
        sel = Selector(text=news_body[0])

        news_links = sel.xpath('//a/@href').extract()
        for link in news_links:
            url = response.urljoin(link)
            yield Request(url, callback=self.parse_post)

    def parse_post(self, response):
            item = CrawlerItem()
            item['title'] = response.css('.story_art_title::text').extract()[0]
            item['author'] = response.css('.shareBar__info--author::text').extract()[0]

            content_str =''
            contents = response.xpath('//div[@id="story_body_content"]//p/text()').extract()
            for content in contents:
                content_str += content
            item['content'] = content_str

            # Transform issued time to UTC+0
            taipei = pytz.timezone('Asia/Taipei')
            dt_str = response.xpath('//div[@class = "shareBar__info--author"]/span/text()').extract()
            item['issued_date'] = datetime.datetime.strptime(dt_str[0], '%Y-%m-%d %H:%M').replace(tzinfo=taipei)

            return item
