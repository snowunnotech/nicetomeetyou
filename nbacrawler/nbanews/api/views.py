from rest_framework import generics, viewsets

from .serializers import NBANewsModelSerializer
from ..models import NBANewsModel


class NBANewsModelListView(generics.ListAPIView):
    queryset = NBANewsModel.objects.all().order_by('-publish_date')
    serializer_class = NBANewsModelSerializer


class NBANewsModelDetailView(generics.RetrieveAPIView):
    queryset = NBANewsModel.objects.all().order_by('-publish_date')
    serializer_class = NBANewsModelSerializer


class NBANewsModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NBANewsModel.objects.all().order_by('-publish_date')
    serializer_class = NBANewsModelSerializer
