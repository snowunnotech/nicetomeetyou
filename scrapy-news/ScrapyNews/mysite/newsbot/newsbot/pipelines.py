# -*- coding: utf-8 -*-
import os
import json
import pdb
import datetime
from channels.layers import get_channel_layer
from django.forms.models import model_to_dict
from main.models import News
from asgiref.sync import async_to_sync
import asyncio

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

class NewsbotPipeline(object):
    

    def process_item(self, item, spider):
        
        #儲存 News DjangoItem
        item.save()

        # 初始化 channel layer
        channel_layer = get_channel_layer()

        # 取得當前處理的 news <Model Object>
        news = News.objects.get(post_url=item['post_url'])
        
        # 新建一個 Async loop，避免交互影響
        loop = asyncio.get_event_loop()

        # 發送 news json 給該 Group， Group name 已固定為 NEWS_STREAMING_GROUP
        loop.create_task(channel_layer.group_send("NEWS_STREAMING_GROUP", {"type": "add_news", "text_data": json.dumps(model_to_dict(news), default=default)}))
        return item
