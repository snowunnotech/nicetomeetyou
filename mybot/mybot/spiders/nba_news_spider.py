# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import HeadlineItem, ArticleItem


class NbaNewsSpider(CrawlSpider):
    name = "nba_news"
    allowed_domains = ["nba.udn.com"]
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    rules = (
        Rule(
            LinkExtractor(allow=(), restrict_xpaths=('//div[@id="news_body"]//descendant::a',)),
            callback="parse_article",
            follow=True,
        ),
    )

    def parse_article(self, response):
        article_title = response.xpath('//div[@id="story_body_content"]/h1/text()').extract_first()
        article_text = ''.join([
            ''.join(p.xpath('.//descendant-or-self::text()').extract() or ['\n\n'])
            for p in response.xpath('//div[@id="story_body_content"]/descendant::p')
        ])
        head = HeadlineItem(headline_text=article_title)
        head_item = head.save()
        item = ArticleItem(headline=head_item, article_text=article_text)
        item.save()
