from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from news.models import News
from news.serializers import NewsSerializer
# Create your views here.


@csrf_exempt
def news_list(request):
    """
    List all news
    """
    if request.method == 'GET':
        news = News.objects.all().order_by('-datetime')
        serializer = NewsSerializer(news, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def news_detail(request, article_id):
    """
    Retrieve a news.
    """
    try:
        news = News.objects.get(article_id=article_id)
    except News.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewsSerializer(news)
        return JsonResponse(serializer.data)
