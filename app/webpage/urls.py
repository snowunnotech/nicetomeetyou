from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('hello_world/', views.Hello.as_view()),
    path('nba_news_in_focus/', views.NBA_News_In_Focus.as_view()),
    path('nba_news_in_focus_list/', views.NBA_News_In_Focus_List.as_view()),
    url(r'^nba_news_detail/(?P<id>[\w]+)/$', views.NBA_News_Detail.as_view()),
]