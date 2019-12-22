# -*- coding: utf-8 -*-
import scrapy
from nbaCrawler.items import NbacrawlerItem


class NbaSpider(scrapy.Spider):
    name = 'nba_posts'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        posts_url = response.xpath('//div[@id="news_body"]/dl/dt/a/@href').extract()
        base_url = "https://nba.udn.com"

        for post_url in posts_url:
            page_url = base_url + post_url
            yield scrapy.Request(page_url, callback=self.parse_page)

    def parse_page(self, response):
        print('-------------------------------------')
        item = NbacrawlerItem()
        title = response.xpath('//h1[@class="story_art_title"]/text()').extract_first()
        item['title'] = title
        print(title)

        image_url = response.xpath('//figure[@class="photo_center photo-story"]/a/img/@data-src').extract_first()
        item['img_url'] = image_url
        print(image_url)

        content = ""
        content_list = response.xpath('//p/text()|//strong/text()').extract()
        for c in content_list:
            content += c
        item['content'] = content
        print(content)

        publish_date = response.xpath('//div[@class="shareBar__info--author"]/span/text()').extract_first()
        publish_date = publish_date[:10]
        item['publish_date'] = publish_date
        print(publish_date)
        print('-------------------------------------')
        yield item

