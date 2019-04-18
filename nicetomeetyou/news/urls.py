from django.urls import path

from . import views


urlpatterns = [
    path('crawler', views.crawl_news, name='crawler')
]