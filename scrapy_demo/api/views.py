# from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from nbascrap.models import NbaNews
from api.serializers import NbaNewsSerializer


# Create your views here.
class NbaNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NbaNews.objects.all().order_by('-post_datetime')
    serializer_class = NbaNewsSerializer


'''
class NbaNewsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = NbaNews.objects.all()
        serializer = NbaNewsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = NbaNews.objects.all()
        nba_news = get_object_or_404(queryset, pk=pk)
        serializer = NbaNewsSerializer(nba_news)
        return Response(serializer.data)
'''

'''
class NbaNewsViewSet(viewsets.ModelViewSet):
    queryset = NbaNews.objects.all()
    serializer_class = NbaNewsSerializer
'''


