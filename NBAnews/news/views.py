from django.shortcuts import render
from news.models import News
from news.serializers import NewsSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @list_route(methods=['get'])
    def total_news(self, request):
        new_num = len(News.objects.all())
        return Response(new_num, status=status.HTTP_200_OK)

    @list_route(methods=['get'])
    def get_news(self, request):
        page = int(request.query_params.get('page'))
        start = (page -1) * 15
        end = page * 15
        news = News.objects.all().order_by('-date')[start:end]
        result = NewsSerializer(news, many=True)
        return Response(result.data, status=status.HTTP_200_OK)
