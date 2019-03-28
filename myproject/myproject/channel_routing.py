
from channels import route, route_class
from myproject.core.websocket_handler import NewsConsumer

channel_routing = [
    route_class(NewsConsumer, path=r"^/chat/"),
]