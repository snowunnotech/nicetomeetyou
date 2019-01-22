"""nba_news URL Configuration

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
from django.urls import include, path
from rest_framework import routers
from nba_news.nba_news import views

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('all_nba_news/<required_id>', views.all_nba_news),
    path('nba_news_list', views.nba_news_list),
    path('nba_news/<article_id>', views.nba_news),
    path('update_news_data', views.update_news_data),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
