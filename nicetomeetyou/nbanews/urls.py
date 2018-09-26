from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from nbanews.views import news_list, newsapi


router = DefaultRouter()
router.register(r'nba_api', newsapi)

urlpatterns = [
    url(r'^nbanews/', news_list),
    url(r'^newsapi/', include(router.urls))
]
