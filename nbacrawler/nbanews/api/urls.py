from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('nbanews', views.NBANewsModelViewSet)

urlpatterns = [
    url(r'^nbanews/$', views.NBANewsModelListView.as_view(), name='nbanews_list_api'),
    url(r'^nbanews/(?P<pk>\d+)/$', views.NBANewsModelDetailView.as_view(), name='nbanews_detail_api'),
    url(r'^', include(router.urls), name='nbanews_route_api'),
]