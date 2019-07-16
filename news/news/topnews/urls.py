from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Register viewset on router
router = DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('news/', include(router.urls)), # Data response as json datatype by viewset 
    path('', views.homepage, name='index'), # Home page
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'), # Detail of each news
]