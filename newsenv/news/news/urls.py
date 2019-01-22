from django.urls import path,include
from django.contrib import admin
from newsapp import views
urlpatterns = [
    path('', include('newsapp.urls')),
    path('newsapi', views.news_object.as_view(),name = 'newsapi'),
    path('admin/', admin.site.urls),
]