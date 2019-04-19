
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from new.models import new
from new.serializers import NewSerializer


class NewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows NEWS to be viewed or edited.
    """
    queryset = new.objects.all()
    serializer_class = NewSerializer

def newList(request):

    return  render(request, 'new/index.html',{})

class getNewList(ListAPIView):
    lookup_field = 'pk'
    queryset = new.objects.all()
    serializer_class=NewSerializer
class get_news_detail(ListAPIView):
    serializer_class = NewSerializer

    def get_queryset(self):
        queryset = new.objects.all()

        article = self.request.query_params.get('atricle', None)
        print(article)
        if article is not None:
            queryset = queryset.filter(article=article)
        return queryset
