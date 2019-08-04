# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3


class UdnNbaPipeline(object):
    def open_spider(self, spider):
        self.conn = None
        self.conn_cursor = None
        self.setup_db_conn()
        #self.createTables()

    def close_spider(self, spider):
        self.conn.close()

    def setup_db_conn(self):
        #db_file = f"{os.getcwd}/../db.sqlite3"
        print(os.getcwd())
        #self.conn = sqlite3.connect(f"{os.getcwd()}/db.sqlite3")
        self.conn = sqlite3.connect("/Users/trainchen/Dropbox/interviews2019/snowunnotech/nicetomeetyou/mysite/db.sqlite3")
        self.conn_cursor = self.conn.cursor()

    def show_tables(self):
        query = f"""
                    SELECT name FROM sqlite_master
                    WHERE type='table'
                    ORDER BY name;
                """
        self.conn_cursor.execute(query)
        available_tables = (self.conn_cursor.fetchall())
        return available_tables

    def store_to_db(self, item):
        query = f"""
                INSERT INTO news_hotnews VALUES ( {item["id"]}, {item["title"]}", "{item["url"]}", "test text" )
                """
        print(query)
        try:
            self.conn_cursor.execute(query)
        except sqlite3.IntegrityError as e:
            print(f"Duplicate news: {e}.")
        else:
            print("Data stored into DB.")
        self.conn.commit()

    def close_db_conn(self):
        self.conn.close()

    def process_item(self, item, spider):
        tables = self.show_tables()
        print(f"tables: {tables}")
        self.store_to_db(item)
        return item
