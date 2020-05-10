from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.list_view, name='NBAframework_list'),
#     # blog list by tag
    url(r'^detail/(?P<id>[-\d]+)/$', views.detail_view, name='NBAframework_detail'),
]