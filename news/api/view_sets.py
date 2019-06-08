""" This modules contains view sets for News """
from news.models import News
from news.api.serializers import NewsSerializer

from rest_framework import viewsets

class NewsViewSet(viewsets.ModelViewSet):
    """
    News API endpoint
    """
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
