"""mysite URL Configuration

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
from django.urls import path
from django.conf.urls import include, url
from demo.views import hello_django, get_news_List, topnba
# from rest_framework import routers, serializers, viewsets

urlpatterns = [
    url(r'^$', topnba),
    url(r'^nbaapi$', get_news_List.as_view()),
    url(r'^hello/$', hello_django),
    url('admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),
    # url(r'^nbanews/$',nbanews)
]
