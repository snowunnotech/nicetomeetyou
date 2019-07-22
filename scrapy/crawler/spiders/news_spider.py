from ..items import CrawlerItem
import scrapy
import logging

host_domain = 'https://nba.udn.com'
targets_xpath = '//*[@id="news_list_body"]/dl/dt'
target_xpath = 'a/@href'
title_xpath = '//*[@id="story_body_content"]/h1/text()'
date_time_xpath = '//*[@id="shareBar"]/div[2]/div/span/text()'
author_xpath = '//*[@id="shareBar"]/div[2]/div/text()'
image_source_xpath = '/html/head/meta[@property="og:image"]/@content'
video_source_xpath = '//*[@id="story_body_content"]/span/div[@class="video-container"]/iframe/@src'
content_xpath = '//*[@id="story_body_content"]/span/p/text() | //*[@id="story_body_content"]/span/p/a/strong/text()'

class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/news/']

    def parse(self, response):
        targets = response.xpath(targets_xpath)
        for target in targets:
            url = host_domain + target.xpath(target_xpath).get()
            yield scrapy.Request(url, callback=self.parse_article)

    def parse_article(self, response):
        item = CrawlerItem()
        try:
            item['title'] = response.xpath(title_xpath).get()
            item['date_time'] = response.xpath(date_time_xpath).get()
            item['author'] = response.xpath(author_xpath).get()
            item['image_source'] = response.xpath(image_source_xpath).get()
            item['video_source'] = response.xpath(video_source_xpath).get()
            item['content'] = ''.join(response.xpath(content_xpath).getall())
            item['article_url'] = response.url           
            yield item
        except Exception as e:
            logging.error(str(e))