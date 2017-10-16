from django.http import HttpResponse
from .models import Headline
from .serializers import HeadlineSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import loader


class HeadlineViewSet(generics.ListCreateAPIView):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    @api_view(['GET'])
    def post_collection(request):
        if request.method == 'GET':
            posts = Headline.objects.all()
            serializer = HeadlineSerializer(posts, many=True)
            return Response(serializer.data)

    @api_view(['GET'])
    def post_element(request, pk):
        try:
            post = Headline.objects.get(pk=pk)
        except Headline.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = HeadlineSerializer(post)
            return Response(serializer.data)


def index(request):
    latest_headline_list = Headline.objects.order_by('-pub_date')

    template = loader.get_template('pyscraper/index.html')
    context = {
        'latest_headline_list': latest_headline_list,
    }
    return HttpResponse(template.render(context, request))
