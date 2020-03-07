"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from catalog import views

# Use include() to add paths from the catalog application
# Add URL maps to redirect the base URL to our application
# Use static() to add url mapping to serve static files during development (only)

router = routers.DefaultRouter()
router.register(r'catalog', views.NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', views.index),
    path('detail/<str:slug>/', views.show_detail_news),
    path('', RedirectView.as_view(url='/catalog/')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
