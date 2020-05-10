from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^celerytask/$', views.celeryTask, name='celerytask'),
]