
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
from rest_framework import routers
from webdata import settings
from webdata.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^index/' , index.as_view() , name = 'index'),
    url(r'^news/api/(?P<news_name>\w{1,30})/$' , news_api.as_view() , name = 'APIs'),
] 
