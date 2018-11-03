# -*- coding: utf-8 -*-
from django_redis import get_redis_connection
from errors.general import get_other_error, error_handler
from django.http import JsonResponse
from datetime import datetime, timedelta
import time
import json

def getNewsFeeds():
    # 取得Redis連線
    con = get_redis_connection("default")

    # 取得現在時間(使用UTC與django時間一致)
    now = datetime.utcnow()
    after_one_minute = now - timedelta(minutes=1)

    # 取得一分鐘前的時間
    nowTimeStamp = int(time.mktime(now.timetuple()))
    after_one_minuteStamp = int(time.mktime(after_one_minute.timetuple()))

    # 取得一段時間內所有的news_feeds
    news_feeds = con.zrangebyscore('news_feeds', after_one_minuteStamp, nowTimeStamp)

    # 轉換json純文字至python對象
    for i, news_feed in enumerate(news_feeds):
        news_feeds[i] = json.loads(news_feed)

    return news_feeds

def get_newsfeed(request):
    return_dict = None
    getNewsFeeds()
    try:
        news_feeds = getNewsFeeds()
        return_dict = {
            'data': news_feeds
        }
    # 其他問題
    except Exception as e:
        return_dict = get_other_error()
        error_handler(e)
    finally:
        return JsonResponse(return_dict, safe=False)