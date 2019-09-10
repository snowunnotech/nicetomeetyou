# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector   #結構化下載的結果，可以用來解析  支持正則匹配
from ..items import HotnewsproItem
# from app01.models import HotNews
# from HotNewsPro.items import HotnewsproItem

class HotnewsSpider(scrapy.Spider):
    name = 'HotNews'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/index?gr=www/']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item_list=hxs.select('//div[@id="news_body"]//dt')   #這樣就會找到所有div id="news_body"屬性的標籤
                 # // 就是整體的後代所有子孫的意思    找的屬性名前面要加上一個@    固定用法

        # print("item_list=",item_list)
        for item in item_list:
            href = item.select('.//a/@href').extract_first().strip()   #這樣取得的 是一個span標籤
            title = item.select('.//h3/text()').extract_first().strip()   #這樣取得的 是一個span標籤
            url = "https://nba.udn.com/" + href
            # print("-----------")
            if url :
                # print(url)
                # print(title)
                # print(url)
                item_obj = HotnewsproItem(title=title,url=url)
                yield item_obj    # 把 item 對象，傳遞給 pipeline 做持續化處理
            else:
                print("非BIG項目")

            # v = item.select('.//span[@class="price"]/text()').extract()   #這樣取得的 是一個span標籤的內容，是一個列表
            # v = item.select('.//span[@class="price"]/text()').extract()[0]  # 這樣取得的 是一個span標籤的內容，取得第一個
            # extract() 功能是把 對象  轉換 為 字符串
