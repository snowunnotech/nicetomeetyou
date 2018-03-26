from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from nba.models import News
from nba.serializers import NbaSerializer

from rest_framework import viewsets

# Create your views here.
@permission_classes((AllowAny, ))
class NbaViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-time')
    serializer_class = NbaSerializer