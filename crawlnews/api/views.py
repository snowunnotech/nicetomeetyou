from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from main.models import News
from .models import UserSerializer, NewsSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
