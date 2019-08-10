from django.shortcuts import render

from news.models import hotNews
from news.serializers import HotNewsSerializer
from rest_framework import viewsets

#from . import consumers

# Create your views here.

def getHotList(request):
    hotNewsList = hotNews.objects.all()
    context = {'hotNewsList': hotNewsList}
    return render(request, 'hotlist.html', context)

class HotNewsViewSet(viewsets.ModelViewSet):
    queryset = hotNews.objects.all()
    serializer_class = HotNewsSerializer