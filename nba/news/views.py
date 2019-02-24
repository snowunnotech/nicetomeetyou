from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from news.models import News

from news.serializers import NewsSerializers
from .crawler import getNewsContent

from rest_framework import viewsets

# Create your views here.


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class Get_All_News(APIView):
    def get(self, request):
        news = News.objects.all()
        serialized = NewsSerializers(news, many=True)
        return Response(serialized.data)


def render_news(request):
    return render(request, 'news.html')


def redirect_news(request):
    return redirect("/news")


def crawler(request):
    getNewsContent()
    return HttpResponse('crawling')


def render_page(request, uuid):
    page = News.objects.get(uuid=uuid)
    render_dict = model_to_dict(page)
    return render(request, 'index.html', render_dict)
