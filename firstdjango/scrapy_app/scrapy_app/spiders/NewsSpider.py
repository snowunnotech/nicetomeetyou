from scrapy.spiders import CrawlSpider
from scrapy_app.items import ScrapyAppItem


class MzSpider(CrawlSpider):
    name = 'spider'
    # start_urls = ['http://www.lolmz.com/hot.php']
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        # news = response.xpath('//div[@class="chroma-gallery mygallery"]//img')
        # /html/body/div[1]/div[1]
        titles = response.xpath('//*[@id="news_body"]/dl/dt/a/h3/text()').getall()
        links = response.xpath('//*[@id="news_body"]/dl/dt/a/@href').getall()
        # //*[@id="news_body"]/dl/dt[1]/a/h3
        # //*[@id="news_body"]/dl/dt[2]/a/h3
        # //*[@id="news_body"]
        # //*[@id="news_body"]/dl/dt[1]/a
        # //*[@id="news_body"]/dl/dt[1]/a?
        # //*[@id="news_body"]/dl/dt[2]/a
        
        # print(titles)
        # print(links)
        # https://nba.udn.com

        # for n in news:
        #     title = n.xpath('@h3').extract_first()
        #     link = n.xpath('@href').extract_first()
        #     item = ScrapyAppItem()
        #     item['title'] = title
        #     item['link_url'] = link
        #     print("gggggggg")
        #     print(title)
        #     print(link)
        #     print('\n')
        #     yield item
        for title, link in zip(titles, links):
            item = ScrapyAppItem()
            item['title'] = title
            item['link_url'] = 'https://nba.udn.com'+link
            print(item['title'])
            print(item['link_url'])
            yield item

