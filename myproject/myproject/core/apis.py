
from rest_framework import viewsets, mixins
from rest_framework import permissions

from .models import New
from .serializers import NewSerializer

class NewViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet
    ):
    queryset = New.objects.all().order_by('-create_datetime')
    serializer_class = NewSerializer
