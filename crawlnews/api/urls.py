from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, NewsViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
