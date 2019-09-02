from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()
		async_to_sync(self.channel_layer.group_add)("NewsUpdateGroup", self.channel_name)
		print("WS Connected")

	def disconnect(self, close_code):
		self.channel_layer.group_discard("NewsUpdateGroup", self.channel_name)
		print("WS DC")

	def receive(self, text_data):
		self.send(text_data="{'message': 'Hello client' }")
	
	def NewsUpdateNotification(self, event):
		Notification = "New news incoming! NewsId:" + str(event["NewsId"]) + " NewsTitle:" + event["NewsTitle"]
		self.send(text_data=Notification)
