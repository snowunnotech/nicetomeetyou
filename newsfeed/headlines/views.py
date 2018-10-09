from newsfeed.headlines.models import HeadlinePost
from newsfeed.headlines.serializers import HeadlinePostSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView

# Create your views here.
class HeadlinePostViewSet(viewsets.ModelViewSet):
    queryset = HeadlinePost.objects.all().order_by('-post_date')
    serializer_class = HeadlinePostSerializer

class HeadlinePostAPIView(APIView):
    def get(self, request):
        queryset = HeadlinePost.objects.all().order_by('-post_date')
        serialized = HeadlinePostSerializer(queryset, many=True)
        return Response(serialized.data)

class IndexHTMLView(TemplateView):
	template_name = 'Index.html'
