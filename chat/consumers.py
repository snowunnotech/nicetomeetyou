from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer
import json
import time
import asyncio
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'ops_coffee' #聊天室群組
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, #房間名稱 ops_coffee
            self.channel_name #頻道名稱
        )

        await self.accept()

    async def disconnect(self, close_code): #斷開時觸發
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, #房間名稱
            self.channel_name#頻道名稱
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data) #別人傳送的訊息
        message = text_data_json['message']
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message':  message
            }
        )
    # Receive message from room group
    async def chat_message(self, event):
        message = 'User：' + event['message']
        # Send message to WebSocket

        await self.send(text_data=json.dumps({#自己的訊息
            'message': message
        }))
    async def send_group_msg(self,group_name,message):
        channel_layer = get_channel_layer()
        # Send message to room group
        await channel_layer.group_send(
            'ops_coffee',
            {
                'type': 'chat_message',
                "message": message
            }
        )

