# -*- coding: utf-8 -*-
#
from django.db.models.signals import pre_save, post_save
from django_redis import get_redis_connection
from utils.model_to_json import get_json_from_news
import time

# 當模型預存儲之前，呼叫這個方法，發送信號
def pre_save_func(sender, **kwargs):
    pass

# 當模型被存儲之後，呼叫這個方法，發送信號
def post_save_func(sender, **kwargs):
    con = get_redis_connection("default")

    # 從信號當中取得新聞
    news = kwargs['instance']

    # 轉換新聞的創建時間為數字格式
    timeStamp = int(time.mktime(news.created_date.timetuple()))

    # 取得news的json
    news_json = get_json_from_news(news)

    # 放入有序集合
    con.zadd('news_feeds', timeStamp, news_json)

    # cache.set(news.news_url, news_json, 10)
    print("快取:'" + news.title + "'新聞")

pre_save.connect(pre_save_func)             # models對象保存前觸發callback函數
post_save.connect(post_save_func)           # models對象保存後觸發callback函數