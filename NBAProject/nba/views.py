# Create your views here.
from nba.models import News
from nba.serializers import NewsSerializer
from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse 

# Create your views here.

def base(request):             
    return render(request, 'news/base.html', {})

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('publishedtime')
    serializer_class = NewsSerializer

    
