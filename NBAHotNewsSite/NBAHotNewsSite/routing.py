from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import NBAHotNewsApp.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
	'websocket': AuthMiddlewareStack(
        URLRouter(
            NBAHotNewsApp.routing.websocket_urlpatterns
        )
    ),
})
