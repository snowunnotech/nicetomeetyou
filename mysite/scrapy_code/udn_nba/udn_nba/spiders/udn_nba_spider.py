from scrapy import Spider
from scrapy.selector import Selector
from udn_nba.items import UdnNbaItem

class UdnNbaSpider(Spider):
    name = "udn_nba"
    allowed_domain = ["udn.com"]
    start_urls = ["https://nba.udn.com/nba/index?gr=www"]

    def parse(self, response):
        focus_news = Selector(response)\
                .xpath("//div[@id='news_body' and @class='box_body']/dl/dt")
        for news in focus_news:
            item = UdnNbaItem()
            item["title"] = news.xpath("a/h3/text()").extract()[0]
            print(item["title"])
            item["url"] = news.xpath("a[contains(@href, '/nba/story')]/@href")\
                .extract()[0]
            yield item

        #filename = response.url.split("/")[-2] + '.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)

#//div[@id="news_body"]