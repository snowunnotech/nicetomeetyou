# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from channels.layers import get_channel_layer
from api.models import News
import asyncio
import os

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

class SpiderbotPipeline(object):
    def process_item(self, item, spider):
        item.save()
        ChannelLayer = get_channel_layer()
        loop = asyncio.get_event_loop()
        loop.create_task(ChannelLayer.group_send("Broadcast_Streaming_Group", {"type": "Broadcast", 'message': 'refresh'}))
        return item
