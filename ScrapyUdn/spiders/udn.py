from ..items import ScrapyudnItem
import scrapy
import time
import requests
from bs4 import BeautifulSoup
import json
from urllib import request, parse
import os
import time
import lxml.html
import re
import urllib.parse
from opencc import OpenCC
import pandas as pd
import numpy as np
import csv
import jieba
import pymysql
class UdnSpider(scrapy.Spider):
    name="udn"
    start_urls="https://nba.udn.com/nba/cate/6754/-1/newest/1"
    def start_requests(self): #翻頁
        for i in range(1):
            url = "https://nba.udn.com/nba/cate/6754/-1/newest/{}".format(str(i+1))
            yield scrapy.Request(url=url,
                                 method='GET',
                                 headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'},
                                 callback=self.parse,
                                 dont_filter=True)
    def parse(self, response):
        soup = BeautifulSoup(response.text)#
        article_each = soup.select("div[id='news_list_body']")[0].select("a")
        for article in article_each:#做每一頁
            article_title = article.select("h3")[0].text
            article_url = "https://nba.udn.com/" + article["href"]
            yield scrapy.Request(url=article_url,
                                 method='GET',
                                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'},
                                 callback=self.parse_article,
                                 meta={"article_title":article_title,"article_url":article_url})
    def parse_article(self, response):#做每篇文章
        item = ScrapyudnItem()
        soup = BeautifulSoup(response.text)
        article_info =soup.select("div[class='shareBar__info']")[0].select("div[class='shareBar__info--author']")[0].text
        a = soup.select("span")[7].findAll("p")
        content =''
        for n, i in enumerate(a[1::]):
            content+=i.text
        date=article_info.split(" ")[0]
        joindate="".join(article_info.split(" ")[0].split("-"))
        Time="".join(article_info.split(date)[1][1:6].split(":"))
        item['title'] = (response.meta["article_title"])
        item['link'] = (response.meta["article_url"])
        item['report'] = article_info
        item['content'] = content
        item['time'] = joindate+Time
        yield item
