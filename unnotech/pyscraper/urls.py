from django.conf.urls import url

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HeadlineViewSet

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nba/$', HeadlineViewSet.as_view(), name='list'),
    url(r'^nba/(?P<pk>[0-9]+)/$', HeadlineViewSet.post_element, name='detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
