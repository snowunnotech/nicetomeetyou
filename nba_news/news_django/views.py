from django.shortcuts import render
from rest_framework import viewsets
from .models import News_model
from .serializers import IndexSerializer, DetailsSerializer
from nba_news import settings

# Create your views here.
def index(request):
    return render(request, 'index.html', context={"context_parser":settings.SERVER_IP +"details/"})

def details(request, id):
    return render(request, 'details.html', context={"context_parser": settings.SERVER_IP +"api/details/", "id": id})

class IndexViewSet(viewsets.ModelViewSet):
    queryset = News_model.objects.all()
    serializer_class = IndexSerializer

class DetailsViewSet(viewsets.ModelViewSet):
    queryset = News_model.objects.all()
    serializer_class = DetailsSerializer

    