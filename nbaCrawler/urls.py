from django.urls import path
from . import views
from nbaCrawler.views import IndexView

app_name = 'nbaCrawler'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pid>/content/', views.content, name='content')
]