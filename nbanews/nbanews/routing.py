'''
Created on Jun 19, 2018

@author: s0974129
'''

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter


from django.conf.urls import re_path
from . import consumers

#websocket 的url連結
websocket_urlpattens = [
    
    re_path( r'index', consumers.IndexConsumer),
    
    ]



application = ProtocolTypeRouter({
    
        # Empty for now (http->django views is added by default)
        'websocket' : AuthMiddlewareStack(
            
                URLRouter(
                    
                        websocket_urlpattens
                    )
            
            )
        
    })
