from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . crawlers import Crawler
from . models import News, Notice
from . serializers import NewsSerializer, NoticeSerializer


def crawl_news(request):

    crawler = Crawler()
    crawler.run()

    return HttpResponse("Crawl success.")


@csrf_exempt
def news_list(request):

    if request.method == 'GET':
        news = News.objects.all().order_by('-published_date')
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


def news_list_page(request):
    return render(request, 'news/index.html')


def news_detail_page(request, id):
    context = {"news_id": id}
    return render(request, 'news/detail.html', context)


@csrf_exempt
def notice_status(request):
    if request.method == 'GET':
        notice = Notice.objects.all().order_by('-create_time').first()
        serializer = NoticeSerializer(notice)
        return JsonResponse(serializer.data, safe=False, status=200)
