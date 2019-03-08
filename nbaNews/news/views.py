from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser

from news.models import News, PushToken
from news.serializers import NewsSerializer


def news(request):
    return render(request, 'news/news.html')


@csrf_exempt
def pushTokenCreate(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        if not token:
            return JsonResponse({'msg': 'error'})
        PushToken.objects.get_or_create(token=token)
        return JsonResponse({'msg': 'success'})
    return JsonResponse({'msg': 'error'})

@csrf_exempt
def pushTokenDelete(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        if not token:
            return JsonResponse({'msg': 'error'})
        PushToken.objects.get(token=token).delete()
        return JsonResponse({'msg': 'success'})
    return JsonResponse({'msg': 'error'})


def newsRead(request, id):
    return render(request, 'news/newsRead.html', {'id': id})


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
