"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path

from django.contrib import admin
from news.controllers import import_news, get_news_by_id,\
    get_newes_count, get_newses_dict, get_news_for_table_data
from news.views import index, get_news_view, news_list
from notification.controller import get_newsfeed
from notification.view import news_feeds_index

urlpatterns = [
    # 新聞及時滾動
    # http://127.0.0.1:8000/get_newsfeed/ 引入新聞
    url(r'^get_newsfeed/', get_newsfeed),

    # http://127.0.0.1:8000/news_feeds_index/ 引入新聞
    url(r'^news_feeds_index/', news_feeds_index),

    # http://127.0.0.1:8000 首頁
    url(r'^/', index),

    # http://127.0.0.1:8000/news_list/ 所有新聞頁面
    url(r'^news_list/', news_list),

    # http://127.0.0.1:8000/get_news/id=1 瀏覽特定新聞
    url(r'^get_news/id=(?P<id>\d+)', get_news_view),

    # admin
    # http://127.0.0.1:8000/admin/
    url(r'^admin/', admin.site.urls),

    # API接口
    # http://127.0.0.1:8000/import_news/ 引入新聞
    url(r'^import_news/', import_news),

    # http://127.0.0.1:8000/get_news_for_table_data/
    url(r'^get_news_for_table_data/', get_news_for_table_data),

    # http://127.0.0.1:8000/get_newses_dict/offset=1&limit=1000&desc=1
    url(r'^get_newses_dict/offset=(?P<offset>\d+)&limit=(?P<limit>\d+)&desc=(?P<desc>\d+)', get_newses_dict),

    # http://127.0.0.1:8000/get_newes_count/
    url(r'^get_newes_count/', get_newes_count),

    # http://127.0.0.1:8000/get_news_by_id/id=1 取得新聞
    url(r'^get_news_by_id/id=(?P<id>\d+)', get_news_by_id),
]