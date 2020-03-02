# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import logging
from ..items import NbaNewsItem


class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/cate/6754']

    def __init__(self, category=None, *args, **kwargs):
        super(NbaSpider, self).__init__(*args, **kwargs)
        self.all_article_links = []

    def parse(self, response):
        article_links = self.get_articles_link_in_page(response)
        logging.debug(article_links)
        self.all_article_links += article_links

        logging.debug("Link List:")
        for link in article_links:
            logging.debug(link)
            target_path = response.urljoin(link)
            yield scrapy.Request(target_path, callback=self.parse_article)

        try:
            assert len(article_links) == 10
            logging.debug("Get 10 Article in catelog page.")
        except AssertionError as e:
            logging.warning("hit end? len(article_links) != 10.")

        next_page = response.css(
            '#news_list > div.pagelink > gonext > a:nth-child(1)::attr(href)').get()
        on_page = response.css(
            "#news_list > div.pagelink > gopage > a.on").get()
        on_page = BeautifulSoup(on_page, 'lxml').get_text()
        logging.warning(on_page)
        if next_page != None and on_page != "2":
            logging.info('next page.1')
            yield response.follow(next_page, self.parse)
            logging.info('next page.2')
        else:
            logging.info('Parsing end.')
            logging.debug('FINISH')
            logging.info("length = {}".format(len(all_article_links)))

    
    def parse_article(self, response):
        title = response.css("#story_body_content > h1").get()
        logging.debug("Title= {}".format(title))

        content = response.css("#story_body_content > span").get()
        logging.debug(content)
        item = self.save_db(title, content)
        yield item


    def parse_catalog(self):
        pass

    def get_articles_link_in_page(self, response):
        result_articles = []
        article_items = response.css('#news_list_body dl dt > a::attr(href)')
        result_articles = [item.get() for item in article_items]

        return result_articles

    def save_db(self, title, content):
        item = NbaNewsItem()
        item['title'] = title
        item['content'] = content
        return item
