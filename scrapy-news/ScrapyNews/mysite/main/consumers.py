import json
import uuid
from channels.generic.websocket import AsyncWebsocketConsumer


class MainConsumer(AsyncWebsocketConsumer):

    
    # 客戶端連線至 WS
    async def connect(self):

        # 加入 NEWS_STREAMING_GROUP 群組
        await self.channel_layer.group_add("NEWS_STREAMING_GROUP", self.channel_name)

        await self.accept()

    # 客戶端從 WS 中斷連線
    async def disconnect(self, close_code):

        # 離開 NEWS_STREAMING_GROUP 群組
        await self.channel_layer.group_discard("NEWS_STREAMING_GROUP", self.channel_name)

    async def receive(self, text_data):
        pass

    # 推送有新的新聞的訊息
    async def add_news(self, text_data):

        await self.send(text_data=json.dumps({
            'model': text_data
        }))