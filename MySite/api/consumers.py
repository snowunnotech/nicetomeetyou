import json
from channels.generic.websocket import AsyncWebsocketConsumer


class BroadcastConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("Broadcast_Streaming_Group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("Broadcast_Streaming_Group", self.channel_name)
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        pass

    async def Broadcast(self, message):
        await self.send(text_data=json.dumps({
            'message': message
        }))