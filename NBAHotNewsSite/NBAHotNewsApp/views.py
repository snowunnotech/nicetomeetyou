from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets

from .models import NBAHotNews
from .serializers import NewsSerializer, NewsDetailSerializer

# Create your views here.
class HotNewsViewSet(viewsets.ModelViewSet):
	queryset = NBAHotNews.objects.values('NewsId', 'NewsTitle', 'NewsUpdateDateTime', 'Author', 'ImgFileName').order_by('-NewsUpdateDateTime')
	serializer_class = NewsSerializer

class HotNewsDetailViewSet(viewsets.ModelViewSet):
	queryset = NBAHotNews.objects.values('NewsTitle', 'Author', 'NewsUpdateDateTime', 'NewsDetailContent')
	serializer_class = NewsDetailSerializer

# Create your views here.
def Index(request):
	#HotNewsList = NBAHotNews.objects.values('NewsId', 'NewsTitle', 'NewsUpdateDateTime', 'Author', 'ImgFileName')
	template = loader.get_template('NBAHotNewsApp/Index.html')
	#context = {'HotNewsList':HotNewsList}
	
	return HttpResponse(template.render({},request))

def NewsDetail(request, NewsId):
	template = loader.get_template('NBAHotNewsApp/NewsDetail.html')
	context = {"NewsId":NewsId}
	return HttpResponse(template.render(context, request))
