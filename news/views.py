from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from news.models import News
from news.serializers import NewsSerializer

from rest_framework import viewsets


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)


def index(request):
    query_news = News.objects.all()
    context = {'news': query_news}
    return render(request, 'index.html', context)

