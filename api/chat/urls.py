from django.conf.urls import url

from . import views





urlpatterns = [
    url(r'^$', views.myNBAfeed, name='index'),
    url(r'^delete', views.removeRec,name="restart"),
]