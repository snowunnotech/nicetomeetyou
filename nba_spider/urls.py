from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_news_list', views.get_news_list)
]