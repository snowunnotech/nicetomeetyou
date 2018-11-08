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

    # get news list
    @action(detail='', methods=['get'], url_path='list')
    def get_news_list(self, request):
        option = request.query_params.get('option')
        item_per_page = 2
        start = 0
        end = item_per_page + 1
        news_list = None
        is_end = False
        if option == 'get_first_page':
            news_list = TopNews.objects.all().order_by('-id')[0:item_per_page]
        # Caution!! update don't check return size currently
        elif option == 'update':
            first_id = int(request.query_params.get('first_id'))
            news_list = TopNews.objects.filter(id__gt=first_id).order_by('-id')
        elif option == 'get_next_page':
            last_id = int(request.query_params.get('last_id'))
            news_list = TopNews.objects.filter(id__lt=last_id).order_by('-id')[0:item_per_page]
        result = TopNewsSerializer(news_list, many=True)
        return Response(result.data, status=status.HTTP_200_OK, content_type='json')

    # get news detail
    @action(detail='', methods=['get'], url_path='news')
    def get_news_detail(self, request):
        top_news_id = int(request.query_params.get('id'))
        news = TopNews.objects.get(id=top_news_id)
        # parse news page
        url = news.pageUrl
        page = requests.get(url)
        p = TopNewsDetailParser()
        p.feed(page.text)
        return Response(str(p.html), status=status.HTTP_200_OK, content_type='text/plain')

    @action(detail='', methods=['get'], url_path='check_update')
    def get_news_update(self, request):
        first_id = int(request.query_params.get('first_id'))
        news_list = TopNews.objects.filter(id__gt=first_id)
        return Response(str(len(news_list)), status=status.HTTP_200_OK, content_type='text/plain')