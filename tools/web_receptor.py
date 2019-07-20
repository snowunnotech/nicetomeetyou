import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class Broadcast(WebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.accept("subprotocol")

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data="Hello world!")
        await self.send(bytes_data="Hello world!")

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message', 
                'message': message
            }
        )

    # async def chat_message(self, event):
    #     message = event['message']

    #     # Send message to WebSocket
    #     self.send(text_data=json.dumps({
    #         'message': message
    #     }))