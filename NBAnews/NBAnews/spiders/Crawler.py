import scrapy
from bs4 import BeautifulSoup as soup
from NBAnews.items import NbanewsItem

class NBA_Crawler(scrapy.Spider):
    name = "NBA_Crawler"
    start_urls = ["https://nba.udn.com/nba/cate/6754"]
    
    def parse(self, response):
        domain = "https://nba.udn.com"
        res = soup(response.body)
        news_list = res.select("#news_list_body")[0]
        links = news_list.select("a")  
                               
        for link in links:
            #print(domain + link["href"])
            yield scrapy.Request(domain + link["href"], self.parse_detail)
        
    def parse_detail(self, response):
        res = soup(response.body)
        
        contents = res.select("#story_body_content")[0].find_all("p")[1:]                      
        all_content = ""
        for content in contents:
            all_content += content.text
        
        nba_news_item = NbanewsItem()
        nba_news_item["title"] = res.select(".story_art_title")[0].text
        nba_news_item["image"] = res.select('img[title="Getty Images"]')[0]["data-src"]
        nba_news_item["content"] = all_content
        nba_news_item["time"] = res.select(".shareBar__info--author")[0].select("span")[0].text
        
        return nba_news_item
        
        #title = res.select(".story_art_title")[0].text
        #time = res.select(".shareBar__info--author")[0].select("span")[0].text
        #print(title, time)