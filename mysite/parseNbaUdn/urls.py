from django.urls import path
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='index')),
    path('task', views.task, name='task'),
    path('index', views.index, name='index'),
]

#
# rest framwork setting
#

from django.conf.urls import url, include
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'', views.TopNewsViewSet)

# Wire up our API using automatic URL routing.
urlpatterns += [
    url(r'^', include(router.urls)),
]
