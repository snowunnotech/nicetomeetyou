from newsfeed.headlines.models import HeadlinePost
from newsfeed.headlines.serializers import HeadlinePostSerializer
from rest_framework import viewsets

# Create your views here.
class HeadlinePostViewSet(viewsets.ModelViewSet):
    queryset = HeadlinePost.objects.all()
    serializer_class = HeadlinePostSerializer