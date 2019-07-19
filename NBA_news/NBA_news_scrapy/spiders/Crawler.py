import scrapy
from scrapy.spiders import CrawlSpider
from bs4 import BeautifulSoup as soup
from NBA_news_scrapy.items import NbaNewsScrapyItem

class NBA_Crawler(CrawlSpider):
    name = "crawler"
    start_urls = ["https://nba.udn.com/nba/cate/6754"]
    
    def parse(self, response):
        domain = "https://nba.udn.com"
        res = soup(response.body)
        news_list = res.select("#news_list_body")[0]
        links = news_list.select("a")  
                               
        for link in links:
            yield scrapy.Request(domain + link["href"], self.parse_detail)
        
    def parse_detail(self, response):
        #res = soup(response.body)
        
        #report = res.select(".shareBar__info--author")[0]
        #contents = res.select("#story_body_content")[0].find_all("p")[1:]     
               
        #all_content = ""
        #for content in contents:
        #    all_content += content.text
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
