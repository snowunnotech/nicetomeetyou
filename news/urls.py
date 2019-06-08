from django.urls import path, re_path, include

from news import views

app_name = 'news'

urlpatterns = [
    path(r'index/', views.index, name='index'),
]

