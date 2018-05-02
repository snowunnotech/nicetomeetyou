from News import views

channel_routing = {
    'websocket.connect': views.ws_connect,
    'websocket.receive': views.ws_receive,
    'websocket.disconnect': views.ws_disconnect,
}