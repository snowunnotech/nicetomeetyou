from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('<int:NewsId>/', views.NewsDetail, name='NewsDetail'),
]
