from django.urls import path

from . import views


urlpatterns = [
    path('api/news', views.news_list, name='news_list'),
    path('api/news/<int:id>', views.news_detail, name='news_detail'),
    path('crawler', views.crawl_news, name='crawler'),
    path('news', views.news_list_page, name='news_list_page'),
    path('news/<int:id>', views.news_detail_page, name='news_detail_page'),
    path('news/notice', views.notice_status, name="notice_status")
]