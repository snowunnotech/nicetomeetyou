from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'news'

router = routers.DefaultRouter()
router.register(r'', views.NewsViewSet)

urlpatterns = [
    path('v1', views.news),
    path('v2', include(router.urls))
]