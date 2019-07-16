from django.shortcuts import render_to_response
from news.models import News
from news.serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import viewsets


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

def News(request):
    return render_to_response('nba.html')
