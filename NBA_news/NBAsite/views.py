from django.shortcuts import render
from django.views.generic.base import View
from NBAsite import models
from NBAsite.serializers import NbaSerializer
from rest_framework import viewsets

# for django homepage
class NBAview(View):
    def get(self, request):
        newsInfo = models.NewsInfo.objects.all().order_by('-time')
        return render(request, 'index.html', locals())
        
# DRF Viewset
class NbaViewSet(viewsets.ModelViewSet):
    queryset = models.NewsInfo.objects.all().order_by('-time')
    serializer_class = NbaSerializer 