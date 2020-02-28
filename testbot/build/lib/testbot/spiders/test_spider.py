import scrapy
from testbot.items import TestbotItem
from bs4 import BeautifulSoup
import time
import requests
from crawler.models import nba_news


class NewsSpider(scrapy.Spider):
    name = "newsSpider"
    news_urls = [
        'https://nba.udn.com/nba/index?gr=www',
    ]
    def parse(self, response):
        item = TestbotItem()
        res = requests.get(url)
        soup = BeautifulSoup(res.text,"html.parser")
        for news in response.css("#news_body a"):
            item['nba_url'] = response.urljoin(news.css("a::attr(href)").get())
            item['nba_title'] = news.css("h3::text").get()
            item['nba_content'] = news.css("img::attr(src)").get()
            yield item
            print(news_title)
            print(news_url)            

        # for news in soup.find('div', id='news_body').find_all('dt'):
        #     if news.find('h3'):
        #         news_title=news.find('h3').text

    #             news_url='https://nba.udn.com'+news.find('a').get('href')

    #             pre_time=''.join([x for x in news.find('b').text if x.isdigit()])
    #             if '小時' in news.find('b').text:
    #                 news_time=time.strftime("%Y/%m/%d, %H:%M", time.localtime(time.time()-int(pre_time)*60*60))
    #             elif '分鐘' in news.find('b').text:
    #                 news_time=time.strftime("%Y/%m/%d, %H:%M", time.localtime(time.time()-int(pre_time)*60))
    #             else:
    #                 news_time=time.strftime("%Y/%m/%d, %H:%M", time.localtime(time.time()-int(pre_time)))

    #             news_content=news.find('p').text

    #             item['nba_title']=news_title
    #             item['nba_url']=news_url
    #             item['nba_time']=news_time
    #             item['nba_content']=news_content
    #             print(news_title)
    #             print(news_url)
    #             print(news_time)
    #             print(news_content)

    #             yield item
    # def parse(self, response):
    #     item = TestbotItem()
    #     for news in response.css("#news_body a"):
    #         item['nba_url'] = response.urljoin(news.css("a::attr(href)").get())
    #         item['nba_title'] = news.css("h3::text").get()
    #         item['nba_content'] = news.css("img::attr(src)").get()
    #         yield item



    	# for news in response.css("#news_body a"):
     #        item['nba_url'] = response.urljoin(news.css("a::attr(href)").get())
     #        item['nba_title'] = news.css("h3::text").get()
     #        item['nba_img'] = news.css("img::attr(src)").get()
     #        yield item
    # def parse(self, response):
    #     posts_url = response.xpath('//div[@id="news_body"]/dl/dt/a/@href').extract()
    #     base_url = "https://nba.udn.com"

    #     for post_url in posts_url:
    #         page_url = base_url + post_url
    #         yield scrapy.Request(page_url, callback=self.parse_page)

    # def parse_page(self, response):
    #     print('-------------------------------------')
    #     item = TestbotItem()
    #     title = response.xpath('//h1[@class="story_art_title"]/text()').extract_first()
    #     item['nba_title'] = title
    #     print(title)

    #     image_url = response.xpath('//figure[@class="photo_center photo-story"]/a/img/@data-src').extract_first()
    #     item['nba_url'] = image_url
    #     print(image_url)

    #     content = ""
    #     content_list = response.xpath('//p/text()|//strong/text()').extract()
    #     for c in content_list:
    #         content += c
    #     item[news_content] = content
    #     print(content)

    #     print('-------------------------------------')
    #     yield item