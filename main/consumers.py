from channels.generic.websocket import AsyncJsonWebsocketConsumer


class EchoConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("news", self.channel_name)
        print(f"Added {self.channel_name} to list")

    async def disconnect(self, code):
        await self.accept()
        await self.channel_layer.group_discard("news", self.channel_name)
        print(f"Removed {self.channel_name} to list")

    async def news_update(self, event):
        await self.send_json(event)  # broadcast this event
        print(f"Got massage {event} at {self.channel_name}")
