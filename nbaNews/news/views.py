from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser

from news.models import News
from news.serializers import NewsSerializer


def news(request):
    return render(request, 'news/news.html')


def newsRead(request, id):
    return render(request, 'news/newsRead.html', {'id':id})

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-uploadDatetime')
    serializer_class = NewsSerializer
    parser_classes = (JSONParser,)
    pagination_class = StandardResultsSetPagination

    # def get_queryset(self):
    #     isShow = self.request.query_params.get('isShow', None)
    #     filterDict = {}
    #     if isShow:
    #         filterDict.update({'isShow': isShow})
    #     return self.queryset.filter(**filterDict)
