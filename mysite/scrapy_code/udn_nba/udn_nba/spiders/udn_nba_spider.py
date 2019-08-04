import uuid
from scrapy import Spider
from scrapy.selector import Selector
from udn_nba.items import UdnNbaItem

class UdnNbaSpider(Spider):
    """
    todo: add another parser for scraping the article contents
    """

    name = "udn_nba"
    allowed_domain = ["udn.com"]
    url_prefix = "https://nba.udn.com"
    start_urls = ["https://nba.udn.com/nba/index?gr=www"]

    def parse(self, response):
        focus_news = Selector(response)\
                .xpath("//div[@id='news_body' and @class='box_body']/dl/dt")
        for news in focus_news:
            item = UdnNbaItem()
            item["title"] = news.xpath("a/h3/text()").extract()[0]
            print(item["title"])
            item["url"] = self.url_prefix + news.xpath("a[contains(@href, '/nba/story')]/@href")\
                .extract()[0]
            item["id"] = uuid.uuid3(uuid.NAMESPACE_URL, item["url"])
            yield item
        #filename = response.url.split("/")[-2] + '.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)

#//div[@id="news_body"]
