from rest_framework import generics, viewsets

from NBAframework.serializers import NBAframeworkSerializer
from ..models import NBAframework


class NBANewsModelListView(generics.ListAPIView):
    queryset = NBAframework.objects.all().order_by('-publish_date')
    serializer_class = NBAframeworkSerializer

class NBANewsModelDetailView(generics.RetrieveAPIView):
    queryset = NBAframework.objects.all().order_by('-publish_date')
    serializer_class = NBAframeworkSerializer

class NBANewsModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NBAframework.objects.all().order_by('-publish_date')
    serializer_class = NBAframeworkSerializer
