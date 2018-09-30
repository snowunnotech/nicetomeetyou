"""
Definition of urls for nicetomeetyou.
"""

from datetime import datetime
from django.urls import path
import app.views


urlpatterns = [
    path('',app.views.home,name='home'),
    path('api/getclecrawler',app.views.getclecrawler),
    path('api/getnewslist', app.views.getnewslist),
    path('api/getnewsdetail/<int:id>',app.views.getnewsdetail)
]
