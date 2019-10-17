# -*- coding: utf-8 -*-

from NbaScrapy.NbaScrapy.NbaScrapy.items import NbascrapyItem
import scrapy
import time
import datetime
import sqlite3

db_name='db.sqlite3'

def CheckText(meg):
    meg=str(meg)
    meg = meg.replace("'","''")
    return meg

def execute_db(fname,sql_cmd):
    conn=sqlite3.connect(fname)
    c=conn.cursor()
    c.execute(sql_cmd)
    try:
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def select_db(fname, sql_cmd):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    c.execute(sql_cmd)
    rows = c.fetchall()
    conn.close()
    return rows

class NbaSpider(scrapy.Spider):
    name = 'NBA'
    allowed_domains = ['nba.udn.com']
    url = 'https://nba.udn.com'
    index_page = '/nba/index'
    start_urls = [url + index_page]

    def parse(self, response):
        url_list = response.xpath('//div[@id="news_body"]/dl/dt/a/@href').extract()

        for story_page in url_list:
            yield scrapy.Request(self.url + story_page, callback=self.parse_detail, encoding='utf-8')

    def parse_detail(self, response):
        item = NbascrapyItem()

        body_content = response.xpath('//div[@id="story_body_content"]')

        item['title'] = body_content.xpath('./h1[@class="story_art_title"]/text()').extract_first()
        item['publish_date'] = body_content.xpath('.//div[@class="shareBar__info--author"]/span/text()').extract_first()
        item['author'] = body_content.xpath('.//div[@class="shareBar__info--author"]/text()').extract_first()
        item['image_url'] = body_content.xpath('//figure/a/img/@data-src').extract_first()
        item['image_caption'] = body_content.xpath('.//figure/figcaption/text()').extract_first()
        item['video_url'] = body_content.xpath('.//div[@class="video-container"]/iframe/@src').extract_first()
        # item['content'] = ','.join(body_content.xpath('.//p').extract())

        content_list = []
        # skip the first wrong extraction
        for p in body_content.xpath('.//p')[1:]:
            s = p.xpath('string(.)').extract_first().strip()
            if s != '':
                content_list.append(s)
        item['content'] = ','.join(content_list)


        sql = str.format("select title from NBAframework_nbaframework where  title='{0}' ",item['title'])
        if not select_db(db_name,sql):
            sql = " insert into NBAframework_nbaframework (title,publish_date,author,image_url,image_caption,video_url,content,read,slug,created) "
            sql += str.format(' values ("{0}","{1}","{2}","{3}","{4}","{5}","{6}",{7},"{8}","{9}") ',
                              item['title'],item['publish_date'],item['author'],item['image_url'],item['image_caption'],item['video_url'],item['content'],True,item['title'],datetime.datetime.today())
            execute_db(db_name,sql)


        yield item