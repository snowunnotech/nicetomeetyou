from channels import Group

# Connected to websocket.connect
def ws_connect(message):
    # Accept the incoming connection
    message.reply_channel.send({"accept": True})
    # Add them to the news_updated group
    Group("users").add(message.reply_channel)

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("users").discard(message.reply_channel)

