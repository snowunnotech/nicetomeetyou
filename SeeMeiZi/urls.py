"""SeeMeiZi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from index.views import FeedsView, Homepage, Get_News_List, Detailpage
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', Get_News_List, 'news')



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hotnews/$', Homepage),
    url(r'^api/', include(router.urls)),
]
urlpatterns += [
    path('', RedirectView.as_view(url='/hotnews/', permanent=True)),
]
urlpatterns += [
    path(r'hotnews/<int:pk>',Detailpage),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

