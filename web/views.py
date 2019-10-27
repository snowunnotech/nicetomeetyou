from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import NewsSerializer
from .models import news

class NewsViewSet(viewsets.ModelViewSet):
    queryset = news.objects.all()
    serializer_class = NewsSerializer
    print(queryset)

def index(request):
    return render(request, 'index.html', )