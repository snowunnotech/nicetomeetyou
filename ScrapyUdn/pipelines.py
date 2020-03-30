# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings
from twisted.enterprise import adbapi
import time
import pandas as pd
import asyncio
import sys
import os


class ScrapyudnPipeline(object): #存進MYSQL
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def __init__(self):
        # 1. 建立資料庫的連線
        self.connect = pymysql.connect(
            # localhost連線的是本地資料庫
            host='127.0.0.1',
            # mysql資料庫的埠號
            port=3306,
            # 資料庫的使用者名稱
            user='root',
            # 本地資料庫密碼
            passwd='aaaa',
            # 表名
            db='udn',
            # 編碼格式
            charset='utf8'
        )
        # 2. 建立一個遊標cursor, 是用來操作表。
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 3. 將Item資料放入資料庫，預設是同步寫入。
        TableName="udn"
        dbname='udn'
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(dbname))  # 若沒有DB創建一個
        COLstr=''
        ColumnStyle = ' VARCHAR(2000)'
        for key in item.keys():
            COLstr=COLstr+' '+key+ColumnStyle+','
        try:
            self.cursor.execute("SELECT * FROM {}".format(TableName))  #若沒有Table創一個
        except:
            self.cursor.execute("CREATE TABLE {} ({})".format(TableName, COLstr[:-1]))
        self.cursor.execute("""select * from udn.udn where link=%s""",item['link'])
        repetition = self.cursor.fetchone()
        if repetition: #弱是沒存過存進去
            pass
        else:
            insert_sql = "INSERT INTO udn(title,link,report,content,time) VALUES ('%s','%s','%s','%s','%s')"%(item["title"], item['link'], item['report'], item['content'], item['time'])
            self.cursor.execute(insert_sql)
            # 4. 提交操作
            self.connect.commit()
        spider.crawler.engine.close_spider(spider)
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()