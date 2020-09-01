"""mucha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from news.views import demo_one, demo_two, demo_three, demo_four

urlpatterns = [
    
    path('demo_one', demo_one ),
    
    path('demo_two', demo_two ),
    
    path('demo_three', demo_three ),
    
    path('demo_four', demo_four ),
    
]
