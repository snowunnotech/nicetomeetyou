from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import HotNewsSerializer
from api.models import HotNews


class HotNewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HotNews.objects.all().order_by('post_date')
    serializer_class = HotNewsSerializer
