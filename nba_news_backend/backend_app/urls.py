"""
./backend_app/urls.py
backend_app URL Configuration
Url patterns for ./backend_app/views.py
"""
from django.urls import re_path, path
from . import views

app_name = 'api'

urlpatterns = [
    re_path(
        r'^tasks/$',
        views.TaskListView.as_view(),
        name='task_list'
    ),
    re_path(
        r'^tasks/(?P<jobid>[0-9a-z]{32})/$',
        views.TaskDetailView.as_view(),
        name='task_datail'
    ),
    re_path(
        r'^articles/$',
        views.ArticleListView.as_view(),
        name='article_list'
    ),
    path(
        'articles/<int:pk>/',
        views.ArticleDetailView.as_view(),
        name='article_detail'
    ),
    path(
        'articles/count/',
        views.article_count,
        name='article_count'
    ),
]
