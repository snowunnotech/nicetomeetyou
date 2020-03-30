from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
application = ProtocolTypeRouter({
    'websocket': SessionMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns #設定路由
        )
    ),
})