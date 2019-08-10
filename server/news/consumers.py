from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class HotListConsumer(WebsocketConsumer):
    def connect(self):
        self.page_group_name = 'hotList'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.page_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.page_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        title = text_data_json['title']
        href = text_data_json['href']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.page_group_name,
            {
                'type': 'newNews',
                'title': title,
                'href': href,
            }
        )

    # Receive message from room group
    def newNews(self, event):
        title = event['title']
        href = event['href']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'title': title,
            'href': href
        }))