#coding=utf-8
# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        print(' event message:{}'.format(message))
        print('event_type:{}'.format(event['type']))
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

