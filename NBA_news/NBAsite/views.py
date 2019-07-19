from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from NBAsite import models
from NBAsite.serializers import NbaSerializer
from rest_framework import viewsets
from django.http import JsonResponse, Http404
# Create your views here.

class NBAview(View):
    def get(self, request):
        newsInfo = models.NewsInfo.objects.all().order_by('-time')
        return render(request, 'index.html', locals())
        
class NbaViewSet(viewsets.ModelViewSet):
    queryset = models.NewsInfo.objects.all().order_by('-time')
    serializer_class = NbaSerializer