""" This modules contains view sets for News """
from news.models import News
from news.api.serializers import NewsSerializer, NewsDetailSerializer

from rest_framework import viewsets

class NewsViewSet(viewsets.ModelViewSet):
    """
    News API endpoint
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_serializer_class(self):
        action = self.action
        if action == 'list':
            return NewsSerializer
        elif action == 'retrieve':
            return NewsDetailSerializer
        return NewsSerializer

    def get_queryset(self):
        pk = self.request.query_params.get('pk')

        if not pk:
            return News.objects.all()
        return News.objects.filter(id=pk).first()

