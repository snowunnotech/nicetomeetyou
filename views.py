from stock.models import Stock
from django.shortcuts import render, redirect
from django.views import generic
from stock.serializers import StockSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .crawler import create_save

# Create your views here.

class Index(generic.ListView):
    model = Stock
    context_object_name = 'stocks'
    template_name = 'about.html'

# REST
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


# RESR Read
class Get_news_List(APIView):
    def get(self, request):
        stock = Stock.objects.all()
        serialized = StockSerializer(stock, many=True)
        return Response(serialized.data)

# Crawler
def click_crawler(request):
    url = 'https://nba.udn.com/nba/cate/6754'
    create_save(url)
    return redirect("/")
