from django.shortcuts import render
import requests

from .models import TopNews
from .parser import TopNewsParser

# Create your views here.

# parse top news title and link then save to database
def task(request):
    url = 'https://nba.udn.com/nba/index?gr=www'
    page = requests.get(url)
    p = TopNewsParser(url)
    p.feed(page.text)
    for n in p.newsList:
        try:
            TopNews.objects.get(postId=n.postId)
        except TopNews.DoesNotExist:
            TopNews(postId=n.postId, title=n.title, imgUrl=n.imgUrl, pageUrl=n.pageUrl).save()
        finally:
            pass

def index(request):
    return render(request, 'index.html')

from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import TopNewsSerializer
from rest_framework.response import Response
from django.http import JsonResponse

class TopNewsViewSet(viewsets.ModelViewSet):
    queryset = TopNews.objects.all()
    serializer_class = TopNewsSerializer

    @action(detail='', methods=['get'], url_path='test')
    def get_news_list(self, request):
        page = int(request.query_params.get('page'))
        # page = 1
        itemPerPage = 2
        start = (page - 1) * itemPerPage
        end = page * itemPerPage
        image = TopNews.objects.all().order_by('-id')[start:end]
        result = TopNewsSerializer(image, many=True)
        # return Response(result.data, status=status.HTTP_200_OK)
        return JsonResponse(result.data, safe=False)
