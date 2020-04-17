from django.urls import path
from nba_news.consumers import NewsConsumer


websocket_urlpatterns = [
    path('ws/get_news/', NewsConsumer),
]
