from django.conf.urls import url
from news import views

urlpatterns = [
    url(
        r'^NewsList/$',
        views.NewsList.as_view(),
        name="NewsList"
    ),
    url(
        r'^NewsDetail/(?P<id>\d+)/$',
        views.NewsDetail.as_view(),
        name="NewsDetail"
    ),
    url(
        r'^',
        views.Index.as_view(),
        name="Index"
    ),
]