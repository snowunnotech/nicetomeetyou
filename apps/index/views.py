from django.shortcuts import render
from django.views.generic.base import View
from .models import Feeds, News
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import NewsSerializer
from django.conf import settings


# Create your views here.

import time, os, subprocess

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from scrapy.cmdline import execute



scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

@register_job(scheduler, "interval", seconds = 3600)
def test_job():
    #time.sleep(4)
    os.chdir(settings.SCRAPY_ROOT)
    p = subprocess.Popen('scrapy crawl spider'.split())
    print (settings.SCRAPY_ROOT)
    p.wait()
    #time.sleep(4)
    print("job complete!")
    # raise ValueError("Olala!")

register_events(scheduler)

scheduler.start()
print("Scheduler started!")



class FeedsView(View):
    def get(self, request):
        all_feeds = Feeds.objects.all()
        return render(request, 'index.html', {'all_feeds': all_feeds})

class Get_News_List(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer   
    def get(self, request):
        news_list = News.objects.all()
        serialized = NewsSerializer(news_list, many=True)
        return Response(serialized.data)


def Homepage(request): # news list page
    return render(request, 'news_list.html')

def Detailpage(request,pk):
	if not News.objects.filter(id = pk):
	    return render(request, 'news_list.html')
	
	context = {
	'id':pk
	}
	return render(request, 'news_detail.html',context = context)

