from django.urls import path

from . import views


urlpatterns = [
    path('', views.news_list),
    path('<int:id>', views.news_detail),
    path('crawler', views.crawl_news, name='crawler')
]