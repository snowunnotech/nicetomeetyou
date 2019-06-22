from drf_test.models import Nba
from drf_test.serializers import NbaSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render


# Create your views here.
class NbaViewSet(viewsets.ModelViewSet):
    queryset = Nba.objects.all().order_by('-rel_date')
    serializer_class = NbaSerializer
    # permission_classes = (IsAuthenticated,)


def get_nba_news(request):
    queryset = Nba.objects.all().order_by('-rel_date')
    return render(request, 'drf_test/nba_news.html', {"datalist": queryset})
