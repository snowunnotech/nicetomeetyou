import scrapy

from udn.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['nba.udn.com']
    start_urls = ('', )

    def start_requests(self):
        urls = [
            'https://nba.udn.com/nba/index?gr=www',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath('//div[@id="news_body"]/dl/dt/a/@href').extract()
        for url in urls:
            yield scrapy.Request('https://nba.udn.com' + url, callback=self.parse_post)

    def parse_post(self, response):
        item = NewsItem()
        item['datetime'] = response.xpath(
            '//div[@id="shareBar"]//div[contains(@class, shareBar__info--author)]//span/text()').extract_first()
        item['author'] = response.xpath(
            '//div[@id="shareBar"]//div[contains(@class, shareBar__info--author)]/text()').extract_first()
        item['title'] = response.xpath(
            '//div[@id="story_body_content"]/h1/text()').extract_first()
        item['image_url'] = response.xpath(
            '//div[@id="story_body_content"]//span//figure//a/img/@data-src').extract_first()
        item['content'] = ''.join(response.xpath(
            '//div[@id="story_body_content"]//p/text()').extract())
        item['url'] = response.url


        yield item
