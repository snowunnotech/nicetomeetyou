from django.shortcuts import render
from crawlerApp.models import News
from crawlerApp.serializers import NewsSerializer


from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])

def news_list(request):
	if request.method == 'GET':
		#news = News.objects.filter(board__exact = 'NBA', date__lt = '2018/03/01', date__gt = '2018/02/01').order_by('-title')[:5]
		news = News.objects.raw("SELECT * FROM crawlerApp_news LIMIT 100")
		serializer = NewsSerializer(news, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def new(request, newId=None):
	if(newId):
		#new = News.objects.filter(id_exact = newId)
		new = News.objects.raw("SELECT * FROM crawlerApp_news WHERE `id` = %s", [newId])
		serializer = NewsSerializer(new, many=True)
		return Response(serializer.data[0])


def showNews(request):



	return render(request, "news.html", locals())

def showANew(request, newId=None):

	return render(request, "new.html", locals())
