from django.shortcuts import render

# Create your views here.
from warehouse.models import TopNews
from warehouse.serializers import TopNewsSerializer

from rest_framework import viewsets

# Create your views here.

class TopNewsViewSet(viewsets.ModelViewSet):
    queryset = TopNews.objects.all().order_by('-id')
    serializer_class = TopNewsSerializer

def topnews(request):
    topnews = TopNews.objects.all()
    return render(request, 'topnews.html', {topnews:topnews})
