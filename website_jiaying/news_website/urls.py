from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.news_index, name='news_index'),
]