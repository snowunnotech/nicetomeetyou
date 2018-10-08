from newsfeed.headlines.models import HeadlinePost
from newsfeed.headlines.serializers import HeadlinePostSerializer
from rest_framework import viewsets
from django.views.generic import TemplateView

# Create your views here.
class HeadlinePostViewSet(viewsets.ModelViewSet):
    queryset = HeadlinePost.objects.all().order_by('-post_date')
    serializer_class = HeadlinePostSerializer

class IndexHTMLView(TemplateView):
	template_name = 'Index.html'
