#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import HotNews


def index(request):
    return HttpResponse("Hello world!")


@csrf_exempt
@require_http_methods(['GET']) # only get and post
def hotnews(request):
    news = HotNews.object.get(url="https://nba.udn.com/nba/story/6780/3967972")
    return HttpResponse(news.title)
