# -*- coding: utf-8 -*-
# ./nba_news_backend/crawler_app/crawler_app/spiders/nba_spider.py
# Jie-Ting Jiang
from datetime import datetime
import scrapy

class NBASpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['nba.udn.com']

    # constructor
    # We are going to pass these args from our django view.
    # To make everything dynamic, we need to override them inside __init__ method
    def __init__(self, *args, **kwargs):

        super(NBASpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'https://nba.udn.com/nba/index?gr=www',
        ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_article_list)

    def parse_article_list(self, response):
        """
        parser for the article list
        """
        # we are in, turn pages and crawl
        self.logger.info('Got successful response from {}'.format(response.url))

        # get the list for focused news
        for tag_dt in response.xpath('//div[@id="news_body"]/dl/dt'):
            # extract the url
            url = response.urljoin(tag_dt.css('a::attr(href)').extract_first())

            # crawl the content of the title
            yield scrapy.Request(
                url,
                callback=self.parse_article
            )

    # parse ptt article
    def parse_article(self, response):
        """
        parser for articles
        """
        article = {}
        article['url'] = response.url

        # extract article title
        article['title'] = response.xpath(
            '//div[@id="story_body_content"]/h1[@class="story_art_title"]/text()'
        ).extract_first()

        # extract author info
        author_info = response.xpath(
            '//div[@class="shareBar__info--author"]/text()'
        ).extract_first()
        article['author_info'] = author_info

        # extract article date time
        dt_str = response.xpath(
            '//div[@class="shareBar__info--author"]/span/text()'
        ).extract_first()
        # add timezone
        publish_dt = datetime.strptime(
            dt_str+' +0800',
            '%Y-%m-%d %H:%M %z'
        )
        article['publish_dt'] = publish_dt

        # extract article content
        content = ''
        # locate paragraph contents
        tag_ps = response.xpath('//div[@id="story_body_content"]/span/p')
        # Note: some words are inside <a><strong> tags while some are not
        for tag_p in tag_ps.xpath('a/strong/text() | text()').extract():
            content += tag_p.strip()
        article['content'] = content

        # return the items to the pipeline (one article one return)
        return article
