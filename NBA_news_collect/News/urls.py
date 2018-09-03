from django.conf.urls import url
from django.contrib import admin
from News import views



urlpatterns = [
    url(r'^home$', views.homepage),
    url(r'^newsapi$', views.NewsList.as_view()),
    url(r'^newsapi_detail/(?P<id>\d+)/$', views.NewsDetail.as_view()),

 
]