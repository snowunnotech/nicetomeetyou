from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class NewsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            "notify", self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            "notify", self.channel_name)

    def notify_message(self, event):
        # Handles the "notify.message" event when it's sent to us.
        self.send(text_data=event["text"])
