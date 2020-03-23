from rest_framework import viewsets
from django.shortcuts import render, HttpResponse

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

from .models import NBANewsPage
from .serializers import NBASerializer
# from .autoScrapy import crawler

# # Create your views here.
# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), 'default')
# # 設定每60秒執行一次
# @scheduler.scheduled_job("interval", seconds=60, id="scrapy")
# def scrapy():
#     page_crawler = crawler()
#     page_crawler.getData()
#     page_crawler.saveData()

# register_events(scheduler)
# scheduler.start()

def Show(requests, pageindex = None):
    data = NBANewsPage.objects.all().order_by('-id')
    return render(requests, "show.html", locals())

class NBAViewSet(viewsets.ModelViewSet):
    queryset = NBANewsPage.objects.all().order_by('-add_date')
    serializer_class = NBASerializer