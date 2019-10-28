import scrapy
import re
import sqlite3
import os

# Scrapy爬蟲排程
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from twisted.internet.task import deferLater


# ITEM
from NBA.items import NbaItem


# 時間處理
def timeStrHandle(time):
    time = "".join(time.split('-'))
    time = "".join(time.split(':'))
    time = "".join(time.split(' '))
    return time

# 爬蟲


class Nba(scrapy.Spider):
    # scrapy crawl {name}
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    # crawl urls(req)
    start_urls = [
        'https://nba.udn.com/nba/cate/6754/-1/newest/{}'.format(i) for i in range(1, 3)]

    def parse(self, response):
        # xpath
        url_list = response.xpath(
            '//div[@class="box_body"]/dl/dt/a/@href').extract()

        new_list = []

        for url in url_list:
            if('story' in url):
                new_list.append('http://nba.udn.com'+str(url))

        for url in new_list:

            # scrapy.Request crawl detail content      url=> request url   callback=> parse_detail callbackfunction
            yield scrapy.Request(url=url, callback=self.parse_content)

    def parse_content(self, response):
        item = NbaItem()

        title = response.xpath(
            '//h1[@class="story_art_title"]/text()').extract()
        content = response.xpath(
            '//p/text()').extract()
        content = ''.join(content)
        time = response.xpath(
            '//div [@class="shareBar__info"]/div[@class="shareBar__info--author"]/span/text()').extract()
        img = response.xpath(
            '//div[@id="story_body_content"]/span/p/figure/a/img/@data-src'
        ).extract()
        time = timeStrHandle(time[0])
        print(
            '----------------------------------------------------------------------------')

        # 確認資料庫有無資料
        BASE_DIR = os.path.dirname(os.path.dirname(
            os.path.abspath('././NBAnews/')))
        print(BASE_DIR)
        conn = sqlite3.connect(
            os.path.join(BASE_DIR, 'db.sqlite3'))
        c = conn.cursor()
        c.execute('SELECT title FROM main_imgnews WHERE time=%s' % time)
        data = c.fetchall()

        try:
            if(data != []):
                print('This data is existed!!')
            else:
                # 將資料寫入ITEM
                item['title'] = title[0]
                item['content'] = content
                item['time'] = time
                item['img'] = img[0]
                yield item
        except Exception as err:
            print(err)


# 爬蟲排程

# 下次爬蟲 等待時間
def sleep(self, *args, seconds):
    return deferLater(reactor, seconds, lambda: None)


process = CrawlerProcess(get_project_settings())

# crawler endless callback


def _crawl(result, spider):

    deferred = process.crawl(spider)
    deferred.addCallback(lambda result: print(
        'waiting 100 seconds before restart'))
    deferred.addCallback(sleep, seconds=100)
    deferred.addCallback(_crawl, spider)
    return deferred


_crawl(None, Nba)
process.start()
