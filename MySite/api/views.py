from django.shortcuts import render

# Create your views here.
import json

from api.models import News
from api.serializers import NewsSerializer
from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse 
from django.utils.safestring import mark_safe

# Create your views here.

def index(request):             
    return render(request, 'list.html', {})

def news(request, id):             
    return render(request, 'news.html', {})

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('CreateAt')
    serializer_class = NewsSerializer