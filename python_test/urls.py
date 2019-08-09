"""python_test URL Configuration

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
from news import views


router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'newsStory', views.NewsStoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', views.news_view),
    path('api/', include(router.urls)),
    # path('echo_once/', views.echo_once),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'),
]
