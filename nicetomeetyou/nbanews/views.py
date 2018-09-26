from django.shortcuts import render
from django.http import HttpResponse

from nbanews.models import NbaNews

def news_list(request):
    return render(request, 'news_list.html')

def newsapi(request):
    return HttpResponse('hello')
