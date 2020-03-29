from django.urls import path
from api.consumers import BroadcastConsumer

websocket_urlpatterns = [
    path('ws/news/', BroadcastConsumer),
]