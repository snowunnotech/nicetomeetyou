from django.urls import path
from django.conf.urls import url
from . import views, newscrawler

urlpatterns = [

    path('newscrawler', newscrawler.crawler, name='crawler'),
    path('', views.news_list, name='news_list'),
    path('news_list/<int:pk>/', views.news_detail, name='news_detail'),
]