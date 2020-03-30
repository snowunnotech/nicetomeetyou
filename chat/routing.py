from django.urls import path
from chat.consumers import ChatConsumer

websocket_urlpatterns = [ #設定WebWocket
    path('ws/chat/', ChatConsumer),
    # url(r'^ws/msg/(?P<room_name>[^/]+)/$', consumers.AsyncConsumer),
]
