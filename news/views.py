from django.shortcuts import render

from core.constant import INDEX_URL

from news.helpers.scrapy import CrawlerService

def index(request, template='news/index.html'):
    crawler_service = CrawlerService(INDEX_URL)
    crawler_service.run()

    return render(request, template)

def detail(request, pk, template='news/detail.html'):

    context = {
        'pk': pk
    }

    return render(request, template, context)
