# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class HotnewsproPipeline(object):
    def __init__(self,conn_str):   # 把需要的資料初始化
        self.conn_str = conn_str   # 這裡就儲存 連接位置
        self.conn = None           # 存放 資料庫連接
        self.cursor = None

    @classmethod
    def from_crawler(cls, crawler):             # 初始化時候，創建對象，並讀取 連接位置
        conn_str = crawler.settings.get('DB')   # 會去 setting那邊尋找 DB的資料庫設定，儲存方式，這個DB必須大寫
        return cls(conn_str)                    # 創建對象，傳入 儲存位置

    def open_spider(self,spider):                       # 爬蟲開始執行時，被調用
        self.conn = sqlite3.connect(self.conn_str)      # 打開資料庫
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):   # 結束爬蟲關閉時，被調用
        self.cursor.close()
        self.conn.close()             # 關閉資料庫

    def process_item(self, item, spider):
        self.cursor.execute("select count(id) from HotNew_hotnews where url = '%s'" %(item['url']))
        result = self.cursor.fetchone()[0]
        if not result:          # 此URL不存在資料庫時
            item.save()         # 把 item 資料存進資料庫
        return item



