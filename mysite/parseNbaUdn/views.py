from django.shortcuts import render
import requests

from .models import TopNews
from .parser import TopNewsParser, TopNewsDetailParser

# Create your views here.


# parse and save top newses' title, link, thumb img link
def task(request):
    index_url = 'https://nba.udn.com/nba/index?gr=www'
    base_url = 'https://nba.udn.com'
    page = requests.get(index_url)
    p = TopNewsParser()
    p.feed(page.text)
    # reversed saving (newest has newest id)
    for n in reversed(p.news_list):
        try:
            TopNews.objects.get(postId=n.postId)
        except TopNews.DoesNotExist:
            TopNews(postId=n.postId,
                    title=n.title,
                    imgUrl=n.imgUrl,
                    pageUrl=base_url + n.pageUrl
                    ).save()
        finally:
            pass


def index(request):
    return render(request, 'index.html')

from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import TopNewsSerializer
from rest_framework.response import Response

class TopNewsViewSet(viewsets.ModelViewSet):
    queryset = TopNews.objects.all()
    serializer_class = TopNewsSerializer

    @action(detail='', methods=['get'], url_path='list')
    def get_news_list(self, request):
        page = int(request.query_params.get('page'))
        item_per_page = 2
        start = (page - 1) * item_per_page
        end = page * item_per_page
        news_list = TopNews.objects.all().order_by('-id')[start:end]
        result = TopNewsSerializer(news_list, many=True)
        return Response(result.data, status=status.HTTP_200_OK, content_type='json')

    @action(detail='', methods=['get'], url_path='news')
    def get_news_detail(self, request):
        top_news_id = int(request.query_params.get('id'))
        # print(top_news_id)
        news = TopNews.objects.get(id=top_news_id)
        url = news.pageUrl
        # print(url)
        page = requests.get(url)
        p = TopNewsDetailParser()
        p.feed(page.text)
        # print(p.html)
        # return HttpResponse(p.html, content_type="text/plain")
        # result = TopNewsSerializer(newsList, many=False)
        return Response(p.html, status=status.HTTP_200_OK, content_type='text/plain')
        # return JsonResponse(result.data, safe=False)
