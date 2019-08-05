from django.shortcuts import render
from rest_framework import viewsets
from .models import HotNews
from .serializers import HotNewsSerializer


class HotNewsView(viewsets.ModelViewSet):
    queryset = HotNews.objects.all()
    serializer_class = HotNewsSerializer