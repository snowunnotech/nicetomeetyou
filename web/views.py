from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import NewsSerializer
from .models import news
import pandas as pd

class NewsViewSet(viewsets.ModelViewSet):
    queryset = news.objects.all()
    serializer_class = NewsSerializer

def index(request):
    output = []
    nba = pd.DataFrame(news.objects.values())
    
    for i in range(0, len(nba)):
        temp = nba.loc[i]
        if output is None:
            output=[{"title":temp['title'],"content":temp['content']}]
        else:
            output.append({"title":temp['title'],"content":temp['content']})
    return render(request, 'index.html', {"output":output})