import scrapy
from scrapy.spiders import CrawlSpider
from SeeMeiSpider.items import SeemeispiderItem, NewsItem, NewsDetailItem


## current progress
## working on second level: newslist, yet to save anything into django model
##
## goal: dig from homepage, goto newslist page & get title, image, shortdescription, detail link
## finally dig into detail page and get newstext for newsdetail content
##

class MzSpider(CrawlSpider):
    name = 'spider'
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        #img_list = response.xpath('//div[@class="chroma-gallery mygallery"]//img')
        #for img in img_list:
        #    title = img.xpath('@alt').extract_first()
        #    img_url = img.xpath('@src').extract_first()
        #    item = SeemeispiderItem()
        #    item['title'] = title
        #    item['image_url'] = img_url
        #    yield item
        domain = "https://nba.udn.com"
        get_newslist_link = response.xpath('//div[@id="news"]//h1[@class = "box-title"]//a')
        link = get_newslist_link[0].xpath('@href').extract_first()
        print('\n')
        print(domain + link)
        print('\n')

        yield scrapy.Request(domain + link, self.parse_list)

    def parse_list(self, response):
        domain = "https://nba.udn.com"
        newslist = response.xpath('//div[@id="news_list_body"]//dt')
        for news in newslist:

            detail_link = news.xpath('a/@href').extract_first()
            news_title = news.xpath('a/h3/text()').extract_first()
            news_description = news.xpath('a/p/text()').extract_first()
            news_image_url = news.xpath('a/span/img/@data-src').extract_first()

            item = NewsItem()
            item['title'] = news_title 
            item['image_url'] = news_image_url
            item['short_description'] = news_description

            yield item

            #print(detail_link)
            #print(news_image_url)

            #yield scrapy.Request(domain + detail_link, self.parse_detail)

            # there should be 10 news in a page




