from django.urls import path, include
from rest_framework import routers
from .views import NbaNewsViewSet

router = routers.DefaultRouter()
router.register(r'nba_news', NbaNewsViewSet, base_name='nba_news')


# viewsets.ViewSet
# news_list = NbaNewsViewSet.as_view({
#     'get': 'list'
# })
# news_detail = NbaNewsViewSet.as_view({
#     'get': 'retrieve'
# })



urlpatterns = [
    path('', include(router.urls)),

    # viewsets.ViewSet
    # path('news_list', news_list),
    # path('news_detail/<int:pk>', news_detail),
]