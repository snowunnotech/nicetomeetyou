from django.conf.urls import url

from . import views

app_name = 'catch'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^content/', views.content, name='content'),
    # url(r'^show/', views.show, name='show'),
]