from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/news_streaming/', consumers.MainConsumer),
    path('wss/news_streaming/', consumers.MainConsumer),
]
