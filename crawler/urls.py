from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ListNews.as_view(), name='news_list'),
    path('<pk>/', views.RetrieveNews.as_view(), name='news_detail'),
]
