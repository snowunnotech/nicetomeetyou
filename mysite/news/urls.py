from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(r"^api/hotnews/list", views.hotnews, name="hotnewsls"), #列表
    #path(r"")
]
