from django.conf import settings
from django.conf.urls import url,static
from django.views.generic import TemplateView
from myapp import views
from django.urls import path,include
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('app/', views.homepage),
    path('content/', views.content),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]