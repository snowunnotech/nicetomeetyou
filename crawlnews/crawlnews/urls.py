"""crawlnews URL Configuration

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
from django.urls import path, re_path, include
from django.contrib import admin
from django.views.generic import TemplateView
#from main import views as main_views
#from api import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    re_path(r'API/?', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    #path('', include('main.urls')),
    re_path(r'.*', TemplateView.as_view(template_name="index.html")),    
]
