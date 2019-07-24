from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import list_route
import requests, datetime, json

from . crawler import crawler
from . models import News
from . serializers import NewsSerializer


##apscheduler
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler.start()

def time_task():
    a = crawler()
    res = a.write_in_db()
    print({'data':res})

scheduler.add_job(time_task, "cron", id='uni', minute=0, misfire_grace_time=30)
register_events(scheduler)

#helper
def sql_query(**kwargs):
    news_id = kwargs.get('news_id')
    if news_id:
        res = News.objects.raw('SELECT * FROM news WHERE id={}'.format(news_id))
    else:
        res = News.objects.all()[:100]
    return res

def allow_cors(data=None):
    response = HttpResponse(json.dumps({"data":data}))
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response


##ViewSet
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @list_route(methods=['get'])
    def show(self, request):
        news_id = request.query_params.get('news_id', None)
        news_list = sql_query(news_id=news_id)
        serializer = NewsSerializer(news_list, many=True)
        return allow_cors(serializer.data)

    @list_route(methods=['get'])
    def spider(self, request):
        a = crawler()
        res = a.write_in_db()
        #res = a.get_news(0)
        return JsonResponse({'data':res})
