import scrapy
from scrapy.crawler import CrawlerProcess
import json
from datetime import datetime
from nba_news.models import NbaNews
from django.core.management.base import BaseCommand

class NbaNewsSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://nba.udn.com/nba/index?gr=www'
    ]


    #def __init__(self, fn_to_store = 'info_scrapy_try.txt'):
    #    self.fn_to_store = fn_to_store

    def parse(self, response):
        if 'index' in response.url:
            news_list_url = response.css('a.more')[0].css('a::attr(href)').extract_first()
            yield response.follow(news_list_url, callback = self.parse)
        elif 'cate' in response.url:
            for news_url in response.xpath('//div[@id="news_list_body"]//dt//a/@href').extract():
                yield response.follow(news_url, callback = self.parse)
            next_url = response.xpath('//gonext//a[@data-id="right"]/@href').extract_first(default = '')
            if next_url:
                yield response.follow(next_url, callback = self.parse)
        elif 'story' in response.url:
            title = response.css('h1.story_art_title::text').extract_first()
            created = response.css('div.shareBar__info--author span::text').extract_first()
            created = datetime.strptime(created, '%Y-%m-%d %H:%M')
            author = response.css('div.shareBar__info--author::text').extract_first()
            photo = response.css('figure img::attr(data-src)').extract_first(default = '').split('&')[0]
            video = response.css('div.video-container iframe::attr(src)').extract_first(default = '')
            context = ''.join(response.css('div#story_body_content span p *::text').extract()[4:])
            nnm = NbaNews(
                created = created,
                title = title,
                author = author, 
                context = context,
                photo = photo,
                video = video
            )
            nnm.save()
            
        """
        for news in response.xpath('//div[@id="news_body"]//dt'):
            #dict_info = {
            yield {
                'href': news.css('a::attr(href)').extract_first()
                #'text': quote.css('span.text::text').extract_first(),
                #'author': quote.css('span small::text').extract_first(),
                #'tags': quote.css('div.tags a.tag::text').extract(),
            }
            #f_to_store.write(json.dumps(dict_info))
        """
        #next_page = response.css('li.next a::attr(href)').extract_first()
        #if next_page is not None:
        #    yield response.follow(next_page, callback=self.parse)

class Command(BaseCommand):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    
    process.crawl(NbaNewsSpider)
    process.start() # the script will block here until the crawling is finished
