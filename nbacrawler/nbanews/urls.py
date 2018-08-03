from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.list_view, name='nbanews_list'),
#     # blog list by tag
    url(r'^detail/(?P<slug>[-\d]+)/(?P<id>[-\d]+)/$', views.detail_view, name='nbanews_detail'),
]