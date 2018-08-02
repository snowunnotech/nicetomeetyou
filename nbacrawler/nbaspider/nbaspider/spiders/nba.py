# -*- coding: utf-8 -*-
import scrapy

from nbaspider.nbaspider.items import NbaspiderItem


class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    url = 'https://nba.udn.com'
    index_page = '/nba/index'
    start_urls = [url + index_page]

    def parse(self, response):
        url_list = response.xpath('//div[@id="news_body"]/dl/dt/a/@href').extract()

        for story_page in url_list:
            yield scrapy.Request(self.url + story_page, callback=self.parse_detail)

    def parse_detail(self, response):
        item = NbaspiderItem()

        body_content = response.xpath('//div[@id="story_body_content"]')

        item['title'] = body_content.xpath('./h1[@class="story_art_title"]/text()').extract_first()
        item['publish_date'] = body_content.xpath('.//div[@class="shareBar__info--author"]/span/text()').extract_first()
        item['author'] = body_content.xpath('.//div[@class="shareBar__info--author"]/text()').extract_first()
        item['image_url'] = body_content.xpath('//figure/a/img/@data-src').extract_first()
        item['image_caption'] = body_content.xpath('.//figure/figcaption/text()').extract_first()
        item['video_url'] = body_content.xpath('.//div[@class="video-container"]/iframe/@src').extract_first()
        contents = body_content.xpath('.//p/text() | .//strong/text()').extract()

        content_list = []
        for content in contents:
            if '。' in content:
                content = content + ','
            content_list.append(content)

        item['content'] = ''.join(content_list)

        print(item['content'])

        yield item
