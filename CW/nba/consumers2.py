#coding=utf-8
import datetime
import pytz

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

# from nba.models import Get_room_name,From_username_to_Pid,Get_room_name,Save_Messages

class NoteficationConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['who_u_fire']
        self.room_group_name = 'chat_%s' % self.room_name
        print('url_route:{}'.format(self.scope['url_route']))
        print('self.channel_name:{}'.format(self.channel_name))
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('text_data_json :{}'.format(text_data_json))
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        print(' event message:{}'.format(message))
        print('event_type:{}'.format(event['type']))
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

