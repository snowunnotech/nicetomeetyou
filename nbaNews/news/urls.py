
from django.urls import path, include

from news import views
from rest_framework import routers

app_name = 'news'
router = routers.DefaultRouter()
router.register('newss', views.NewsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('/<id>/', views.newsRead),
    path('', views.news, name='news'),
]
