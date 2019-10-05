from top_news_bot.items import TopNewsBotItem
import scrapy
from scrapy.utils.markup import remove_tags
from scrapy.spiders import CrawlSpider
from uuid import uuid4


class topNewsSpider(CrawlSpider):

    name = 'top_news_spider'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/index', ]

    def parse(self, response):
        domain_name = 'https://nba.udn.com'
        res = response.css('div#news_body dl dt')
        for news in res:
            url = news.css('a::attr(href)').extract_first()
            if url is not None:
                url = response.urljoin(url)
                yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):

        title = response.css('div#story_body_content')[
            0].css("h1::text")[0].extract()
        unique_id = str(uuid4())
        date = response.xpath(
            '//*[@id="shareBar"]/div[2]/div/span/text()')[0].extract()

        data = response.xpath(
            '//*[@id="story_body_content"]/span/p').getall()[1:]
        data = remove_tags(''.join(data))
        print('###unique_id', unique_id)
        item = TopNewsBotItem()
        item['unique_id'] = unique_id
        item['title'] = title
        item['date'] = date
        item['data'] = data
        yield item
