# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    content = scrapy.Field()
    published_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql="""
            insert into news(title,crawled_time,content,image_url,published_time   
              )VALUES(%s,%s,%s,%s,%s)
        """

        title = self["title"][0]
        crawled_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        published_time = self["published_time"][0]
        image_url = self["image_url"][0]
        content = ''.join(self['content'])

        params = (title, crawled_time, content, image_url, published_time)

        return insert_sql, params
