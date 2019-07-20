from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from tools import web_receptor

application = ProtocolTypeRouter({
    # WebSocket
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^wx/notify/$", web_receptor.Broadcast),
        ])
    ),
})