from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from nba_news import views

router = DefaultRouter()
router.register(r'nba_news', views.NbaNewsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^home$', views.homepage),
    url(r'^story/(?P<news_id>[0-9]+)', views.storypage)
]

