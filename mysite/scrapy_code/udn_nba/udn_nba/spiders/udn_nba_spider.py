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
        print(focus_news)
        for news in focus_news:
            # item = UdnNbaItem()
            # item["title"] = news.xpath("a/h3/text()").extract()[0]
            # print(item["title"])
            # item["url"] = self.url_prefix + news.xpath("a[contains(@href, '/nba/story')]/@href")\
            #     .extract()[0]
            # item["id"] = uuid.uuid3(uuid.NAMESPACE_URL, item["url"])
            # yield item
            if news.css(".ads"):
                continue

            relative_url = news.xpath("a[contains(@href, '/nba/story')]/@href")\
                    .extract()[0]

            news_url = self.url_prefix + relative_url

            item = UdnNbaItem(
                id=str(uuid.uuid3(uuid.NAMESPACE_URL, news_url)),
                title=news.xpath("a/h3/text()").extract()[0],
                url=news_url,
            )      
            if news_url is not None:
                yield response.follow(news_url, callback=self.parse_news_article, meta={"item": item})

    def parse_news_article(self, response):
        def extract_with_css(query):
            elements = response.css(query)
            if len(elements) == 1:
                extracted = elements.get(default='').strip()
            else:
                extracted = elements.extract()
                print(extracted)
            return extracted

        item = response.meta.get("item")
        item.update(
            #publish_datetime=extract_with_css("div.shareBar__info--author span::text"),
            published_datetime=extract_with_css("div.shareBar__info--author ::text")[0],
            author=extract_with_css("div.shareBar__info--author ::text")[1],
            contents="\n".join(extract_with_css("#story_body_content > span > p::text"))
            # publish_datetime=response.css("div.shareBar__info--author ::text")[0].get(),
            # author=response.css("div.shareBar__info--author ::text")[1].get(),
            # contents="\n".join(extract_with_css("#story_body_content > span > p::text"))
        )
        print(item)
        # yield item.update(
        #     author=extract_with_css("div.shareBar__info--author span::text"),
        #     #publish = extract_with_css(),
        # )
        yield item

#//div[@id="news_body"]
