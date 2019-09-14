import scrapy
from w3lib.html import remove_tags, remove_tags_with_content
from NewsCrawler.items import ArticleItem


class NewsCrawler(scrapy.Spider):
    name = "NewsCrawler"
    allowed_domains = ['nba.udn.com']
    start_urls = [
        "https://nba.udn.com/nba/index?gr=www",
    ]

    def parse(self, response):
        news_list = response.xpath(
            '//*[@id="news_body"]//dl//a/@href').getall()
        for url in news_list:
            yield response.follow(url, callback=self.parse_news)

    def parse_news(self, response):
        input = ''.join(response.xpath(
            '//*[@id="story_body_content"]/span/p').extract())
        content = remove_tags(
            remove_tags_with_content(input, ('div', 'figure')), keep=('p',))

        item = ArticleItem()
        item['a_title'] = response.css(
            'h1.story_art_title::text').get()
        item['a_datetime'] = response.css(
            'div.shareBar__info--author span::text').get()
        item['a_source'] = response.css(
            'div.shareBar__info--author::text').get()
        item['a_content'] = content
        yield item
