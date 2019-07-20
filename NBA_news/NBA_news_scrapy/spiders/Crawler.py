import scrapy
from scrapy.spiders import CrawlSpider
from NBA_news_scrapy.items import NbaNewsScrapyItem

# Get NBA news by scrapy and store to DRF items
# Including report title, report time, reporter, report link, report image, report content  
class NBA_Crawler(CrawlSpider):
    name = "crawler"
    start_urls = ["https://nba.udn.com/nba/cate/6754"]
    allowed_domains = ["nba.udn.com"]
    
    def parse(self, response):       
        for link in response.xpath('//*[@id="news_list_body"]/dl/dt/a/@href').extract():
            yield scrapy.Request(response.urljoin(link), self.parse_detail, dont_filter=True)
        
    def parse_detail(self, response):

        Title = response.xpath('//*[@id="story_body_content"]/h1/text()').extract()
        Report = response.xpath('//*[@class="shareBar__info--author"]//text()').extract()
        Image = response.xpath('//*[@class="photo_center photo-story"]/a/img/@data-src').extract()
        Content = response.xpath('//*[@id="story_body_content"]/span/p//text()').extract()
             
        nba_news_item = NbaNewsScrapyItem()
        nba_news_item['news_id'] = response.url.split('/')[-1]
        nba_news_item["title"] = Title[0]
        nba_news_item["time"] = Report[0]
        nba_news_item["reporter"] = Report[1]
        nba_news_item["link"] = response.url
        nba_news_item["image"] = Image[0]
        nba_news_item["content"] = ''.join(Content[4:])
        
        return nba_news_item