import scrapy
from nba_bot.items import NbaBotItem
from bs4 import BeautifulSoup

class NBASpider(scrapy.Spider):
    name = "nba"
    start_urls = [
        'https://nba.udn.com/nba/index?gr=www',
    ]
    
    def parse(self, response):
        domain = "https://nba.udn.com"
        res = BeautifulSoup(response.body)
        news_div = res.find("div", id="news_body")
        for dt in news_div.select("dt"):
            web_link = domain + dt.select("a")[0]["href"]
            yield scrapy.Request(web_link, self.parse_detail)
            
    def parse_detail(self, response):
        res = BeautifulSoup(response.body)
        content_div = res.find("div", id="story_body_content")
        title = content_div.find("h1", class_="story_art_title").text
        publishedtime = content_div.find("div", class_="shareBar__info--author").select("span")[0].text
        
        # 刪除指定區塊
        content_div.find('figure', class_="photo_center photo-story").decompose()
        ps = content_div.select("p")
        content = '\n'.join(p.text for p in ps)
        
        item = NbaBotItem()
        item["title"] = title
        item["publishedtime"] = publishedtime
        item["content"] = content
        item["web_link"] = response.url
        yield item
        