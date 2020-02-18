from django.urls import path

from . import views

urlpatterns = [
    path('get-articles', views.get_list_of_article, name='get_articles'),
    path('detail/<str:slug>', views.article_detail, name='detail'),
    path('', views.index, name='index'),
]