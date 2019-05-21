from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from news import views


router = DefaultRouter()

router.register('news', views.NewsViewSet)
router.register('detail', views.DetailViewSet, base_name='detail')

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^home/', views.home),
    url(r'^detail/(\d+)', views.detail),
]
