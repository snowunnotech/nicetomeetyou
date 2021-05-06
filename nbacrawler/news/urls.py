from django.conf.urls import url
from news import views


urlpatterns = [
    url(r'^news_list/$', views.news_list),
]
