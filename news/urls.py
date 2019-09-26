from rest_framework import routers
from news import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    path('', views.index.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
