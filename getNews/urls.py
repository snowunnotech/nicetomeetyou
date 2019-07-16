"""getNews URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from new.views import NewViewSet,newList, getNewList, get_news_detail

router = routers.DefaultRouter()
router.register(r'news', NewViewSet)
urlpatterns = [
    # path(r'admin/', admin.site.urls),
    path(r'',newList),
    path(r"api",include(router.urls)),
    path(r"getNews/",getNewList.as_view(),name='getNews'),
    path(r'detail',get_news_detail.as_view()),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
