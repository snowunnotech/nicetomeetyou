from django.urls import path
from .views import IndexView, NewsListView, NewsDetail

urlpatterns = [

    path('', IndexView.as_view(), name="index"),
    path('newslist/', NewsListView.as_view(), name="newslist"),
    path('newsdetail/<int:url_id>', NewsDetail, name="newsdetail"),
    
]
