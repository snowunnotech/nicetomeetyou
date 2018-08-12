from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from main.consumers import EchoConsumer


application = ProtocolTypeRouter({
    "websocket": URLRouter([
        # URLRouter just takes standard Django path() or url() entries.
        path("new_post/", EchoConsumer),
    ]),
})
