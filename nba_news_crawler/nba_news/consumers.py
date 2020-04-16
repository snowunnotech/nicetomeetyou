from channels.generic.websocket import WebsocketConsumer
from pytz import timezone
from nba_news.models import NbaNews
from utils.item import Item
import json
import time
import datetime


class NewsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        while True:
            now_time = datetime.datetime.now(timezone('UTC'))
            query_time = now_time - datetime.timedelta(minutes=59)
            query_result = NbaNews.objects.filter(timestamp__gte=query_time)
            items = Item.map(query_result)

            if items:
                response = json.dumps({
                    'data': items
                })
                self.send(text_data=response)
            time.sleep(60 * 60)

    def receive(self, text_data=None, bytes_data=None):
        pass

    def disconnect(self):
        pass
