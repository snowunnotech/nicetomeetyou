from django.shortcuts import render, redirect

import threading

from core.constant import INDEX_URL

from news.helpers.scrapy import CrawlerService

def index(request, template='news/index.html'):
    crawler_service = CrawlerService(INDEX_URL)
    crawler_service.threading_run()

    for thread in threading.enumerate():
        if thread.name == "crawler_service_run":
            print(thread.name)

    return render(request, template)

def detail(request, pk, template='news/detail.html'):

    context = {
        'pk': pk
    }

    return render(request, template, context)

def handler404(request, exception):

    return redirect('news:index')
