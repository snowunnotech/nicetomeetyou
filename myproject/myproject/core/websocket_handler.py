from channels.generic.websockets import WebsocketConsumer

class NewsConsumer(WebsocketConsumer):
    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return ["news"]

    def connect(self, message, **kwargs):
        """
        Perform things on connection start
        """
        # Accept the connection; this is done by default if you don't override
        # the connect function.
        self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        """
        Called when a message is received with either text or bytes
        filled out.
        """
        # Simple echo
        self.send(text=f'Server received: {text}', bytes=bytes)

    def send_update_news(self):
        Group("news").send({
            "news_update": True
        })

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass
