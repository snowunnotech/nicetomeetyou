from django.shortcuts import render
from rest_framework import generics
from .serializers import NewsSerializer
from .models import SpotNews
from django.http import HttpResponse

class NewsViewset(generics.ListCreateAPIView):
	queryset = SpotNews.objects.all()
	serializer_class = NewsSerializer

def index(request):
	news_list = SpotNews.objects.all().order_by('-date')
	return render(request, 'index.html', {'news_list':news_list})

def get_content(request, pk):
	targetnews = SpotNews.objects.all().filter(id=pk).values_list()[0]
	resdata = HttpResponse('<h2><span>'+targetnews[1]+'</span></h2><span>'+\
							str(targetnews[2])[:-6]+'&nbsp&nbsp&nbsp&nbsp'+targetnews[3]+\
							'</span><p><span>'+targetnews[4]+'</span></p>')

	return resdata