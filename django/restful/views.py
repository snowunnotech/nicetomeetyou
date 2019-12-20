from django.shortcuts import render

# Create your views here.
from myapp.models  import news
from restful.serializers import newsSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class newsViewSet(viewsets.ModelViewSet):
    queryset=news.objects.all()
    serializer_class=newsSerializer
    permission_classes=(IsAuthenticated,)