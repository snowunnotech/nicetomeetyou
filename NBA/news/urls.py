from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('news', views.NBANewsViewSet)

app_name = 'news'
urlpatterns = [
    path('api/', include(router.urls)),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>', views.news_detail, name='news_list'),
]

