from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NBANews
from .serializers import NewsListSerializer, NewsSerializer
from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')
settings = {
			'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
		}

# Create your views here.

class GetNewsList(APIView):
	def get(self, request):
		news_list = NBANews.objects.order_by('-date')
		serialized = NewsListSerializer(news_list, many=True)
		return Response(serialized.data)

class GetNews(APIView):
	def get(self, request):
		nid = request.GET['nid']
		try:
			news = NBANews.objects.get(news_id = nid)
			serialized = NewsSerializer(news, many=False)
			return Response(serialized.data)
		except NBANews.DoesNotExist:
			return Response()
		

class CrawlNews(APIView):
	def get(self, request):
		task = scrapyd.schedule('default', 'udn_spider')
		return Response()
		

def UdnNBANews(request):
	return render(request, "udnnbanews.html")