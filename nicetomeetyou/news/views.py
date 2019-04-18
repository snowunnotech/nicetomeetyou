from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . crawlers import Crawler
from . models import News
from . serializers import NewsSerializer

def crawl_news(request):

    crawler = Crawler()
    crawler.run()

    return HttpResponse("Crawl success.")


@csrf_exempt
def news_list(request):

    if request.method == 'GET':
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)


@csrf_exempt
def news_detail(request, id):

    try:
        news = News.objects.get(id=id)
    except News.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewsSerializer(news)
        return JsonResponse(serializer.data)

