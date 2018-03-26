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
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })