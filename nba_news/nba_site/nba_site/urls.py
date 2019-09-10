"""nba_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from django.contrib import admin
from news import views
from news.views import news_view, content_view

router = DefaultRouter()
router.register(r'news_list', views.NewsListViewSet, base_name= 'news_list')
router.register(r'news_detail', views.NewsDetailViewSet, base_name= 'news_detail')


urlpatterns = [
    url(r'^api/news_list_api', views.news_list_api),
    url(r'^api/news_detail_api', views.news_detail_api),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^news/', news_view),
    url(r'^nba_news/', content_view)
]