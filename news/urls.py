from django.conf.urls import url
from django.urls import path
from news import views

app_name = 'news'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^detail/$', views.show_detail, name='detail'),
    url(r'^api/news/$', views.NewsView.as_view(), name="api_news"),
    url(r'^api/news/(?P<pk>[0-9]+)/$', views.NewsDetail.as_view(), name="api_news_detail"),
]