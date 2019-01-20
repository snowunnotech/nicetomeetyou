from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from NBA_news_collect import NBA_news_crawler

def homepage(request):
    NBA_news_crawler.NBA_news_crawler().store_news_info()
    return render(request, 'index.html')



class NewsList(APIView):
    def get(self, request):
        news = News.objects.all()
        serialized = NewsSerializer(news, many=True)
        return Response(serialized.data)





class NewsDetail(APIView):
    def get(self, request, id):
        news_detail = News.objects.filter(id=id)
        serialized = NewsSerializer(news_detail, many=True)
        return Response(serialized.data)