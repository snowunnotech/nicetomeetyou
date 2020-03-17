import scrapy
from nba.items import NbaItem

 
class NbaSpider(scrapy.Spider):
     name = 'nba' 
     allowed_domains = ["udn.com"] 
     start_urls = ["https://nba.udn.com/nba/index?gr=www"]
     domain = "https://nba.udn.com/"
     def parse(self, response):
       
        items = []

        for each in response.xpath("/html/body/div[1]/div[2]/div[8]/div[1]/div/div/dl/dt/a"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = NbaItem()
            #extract()方法返回的都是unicode字符串
            
            
            title = each.xpath("h3/text()").extract()
            date = each.xpath("b/text()").extract()
            content = each.xpath("p/text()").extract()
            #xpath返回的是包含一个元素的列表
            item['title'] = title[0]
            item['date'] = date[0]
            item['content'] = content[0]
            items.append(item)

        # 直接返回最后数据
        return items
