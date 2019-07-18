from django.shortcuts import render
from django.views.generic.base import View
from NBAsite import models
from NBAsite.serializers import NbaSerializer
from rest_framework import viewsets
# Create your views here.

#class NBAview(View):
#    def get(self, request):
#        newsInfo = models.NewsInfo.objects.all()
#        return render(request, 'index.html', locals())

class NbaViewSet(viewsets.ModelViewSet):
    queryset = models.NewsInfo.objects.all()
    serializer_class = NbaSerializer