from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^news_content/', views.news_content_crawler.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)