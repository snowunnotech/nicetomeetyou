from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^news_content/', views.NewsContentCrawler.as_view()),
    url(r'^news_list/', views.NewsListCrawler.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)