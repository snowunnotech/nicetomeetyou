from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from news.models import News
from news.serializers import NewsSerializer

from rest_framework import viewsets


# Create your views here.
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-issued_date')
    serializer_class = NewsSerializer
