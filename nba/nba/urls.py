"""nba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from news import views
from news.views import *

router = DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crawler/', crawler),
    path('api/', include(router.urls)),
    path('news/', render_news),
    path('', redirect_news),
    path('newsapi', Get_All_News.as_view()),
    re_path(r'^news/(?P<uuid>[0-9]+)/$', render_page)
]
