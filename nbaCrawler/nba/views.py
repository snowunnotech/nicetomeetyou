from datetime import datetime

from django.shortcuts import render

from nba.models import News
from nba.serializers import NbaSerializer

from rest_framework import viewsets

# Create your views here.
class NbaViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-time')
    serializer_class = NbaSerializer


def index(request):
    return render(request, 'index.html')

def detail(request, pk):
    return render(request, 'detail.html', {'news': News.objects.get(pk=pk)})