from scrapy import Spider

class UdnNbaSpider(Spider):
    name = "udn_nba"
    allowed_domain = ["udn.com"]
    start_urls = ["https://nba.udn.com/nba/index?gr=www"]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)    