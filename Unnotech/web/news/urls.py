from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^news/$', views.news_list),
    url(r'^news/(?P<article_id>[0-9]+)/$', views.news_detail),
]
