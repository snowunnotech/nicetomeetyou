from django.urls import path

from . import views

app_name = 'udn_news'
urlpatterns = [
    path('', views.index, name='index'),
    path('getContent/<slug:id>', views.getContent, name='getContent'),
]
