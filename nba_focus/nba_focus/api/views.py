from focus.models import News
from rest_framework import viewsets
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows news to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer