from django.shortcuts import render
import requests

from .models import TopNews
from .parser import TopNewsParser, TopNewsDetailParser

# Create your views here.

# parse top news title and link then save to database
def task(request):
    index_url = 'https://nba.udn.com/nba/index?gr=www'
    base_url = 'https://nba.udn.com'
    #
    # need to handle exception here
    #
    page = requests.get(index_url)
    top_news_parser = TopNewsParser()
    top_news_parser.feed(page.text)
    news_detail_parser = TopNewsDetailParser
    for url in top_news_parser.newsUrlList:
        page = requests.get(base_url + url)
        top_news_parser.feed(page.text)
        news_detail_parser()


    # print('task')
    # for n in p.newsList:
    #     try:
    #         TopNews.objects.get(postId=n.postId)
    #     except TopNews.DoesNotExist:
    #         TopNews(postId=n.postId, title=n.title, imgUrl=n.imgUrl, pageUrl=n.pageUrl).save()
    #     finally:
    #         pass

def index(request):
    return render(request, 'index.html')

from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import TopNewsSerializer
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse

class TopNewsViewSet(viewsets.ModelViewSet):
    queryset = TopNews.objects.all()
    serializer_class = TopNewsSerializer

    @action(detail='', methods=['get'], url_path='list')
    def get_news_list(self, request):
        page = int(request.query_params.get('page'))
        itemPerPage = 2
        start = (page - 1) * itemPerPage
        end = page * itemPerPage
        newsList = TopNews.objects.all().order_by('-id')[start:end]
        result = TopNewsSerializer(newsList, many=True)
        # return Response(result.data, status=status.HTTP_200_OK)
        return JsonResponse(result.data, safe=False)

    @action(detail='', methods=['get'], url_path='news')
    def get_news_detail(self, request):
        id = int(request.query_params.get('id'))
        print(id)
        news = TopNews.objects.get(id=id)
        url = news.pageUrl
        print(url)
        page = requests.get(url)
        p = TopNewsDetailParser()
        p.feed(page.text)
        print(p.html)
        return HttpResponse(p.html, content_type="text/plain")
        # result = TopNewsSerializer(newsList, many=False)
        # # return Response(result.data, status=status.HTTP_200_OK)
        # return JsonResponse(result.data, safe=False)
