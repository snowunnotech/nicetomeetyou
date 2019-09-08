from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, mixins, viewsets

from .models import News
from .serializers import NewsDetailSerializer, NewsIndexSerializer

# Create your views here.


def index(request):
    return render(request, 'index.html')


class NewsIndexListViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = News.objects.all().order_by('-published_at')
    serializer_class = NewsIndexSerializer


class NewsDetailViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = NewsDetailSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        queryset = News.objects.all().order_by('-published_at')
        if 'pk' in self.kwargs:
            uid = self.kwargs['pk']
            queryset = queryset.filter(uid=uid)

        return queryset
