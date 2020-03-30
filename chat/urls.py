from django.urls import path,re_path
from . import views
from django.conf.urls import url  #導入url套件
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
app_name = 'chat'
urlpatterns = [
    path(r'',views.chat, name="chat"),
    re_path(r'^ajax/Json_Ajax/$',views.index_Ajax,name="index_Ajax"), #設定下拉的Ajax
    path('<str:title>',views.post_record,name='post_record'),
    path('index/<str:title>', views.post_record, name='post_record'), #設定詳細文章的網址
]