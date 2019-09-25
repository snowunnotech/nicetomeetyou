from django.shortcuts import render
from news.models import Articles
from news.serializers import ArticleSerializer
from rest_framework import viewsets

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


def index(request):
    return render(request, 'index.html')
