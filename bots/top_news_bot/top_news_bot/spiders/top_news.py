from top_news_bot.items import TopNewsBotItem
import scrapy
from scrapy.utils.markup import remove_tags


class nbaSpider(scrapy.Spider):

    name = 'nba_news'
    start_urls = ['https://nba.udn.com/nba/index', ]

    def parse(self, response):
        domain_name = 'https://nba.udn.com'
        res = response.css('div#news_body dl dt')
        for news in res:
            try:
                yield scrapy.Request(domain_name+news.css('a::attr(href)')[0].extract(), self.parse_detail)
            except IndexError:
                pass
        pass

    def parse_detail(self, response):

        title = response.css('div#story_body_content')[
            0].css("h1::text")[0].extract()

        date = response.xpath(
            '//*[@id="shareBar"]/div[2]/div/span/text()')[0].extract()

        data = response.xpath(
            '//*[@id="story_body_content"]/span/p').getall()[1:]
        data = remove_tags(''.join(data))

        item = TopNewsBotItem()
        item['title'] = title
        item['date'] = date
        item['data'] = data
        yield item
