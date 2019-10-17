from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('NBAframework', views.NBANewsModelViewSet)

urlpatterns = [
    url(r'^NBAframework/$', views.NBANewsModelListView.as_view(), name='NBAframework_list_api'),
    url(r'^NBAframework/(?P<pk>\d+)/$', views.NBANewsModelDetailView.as_view(), name='NBAframework_detail_api'),
    url(r'^', include(router.urls), name='NBAframework_route_api'),
]