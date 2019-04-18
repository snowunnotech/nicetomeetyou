import sys
from django.shortcuts import render, HttpResponse
from . import crawlers


def crawl_news(request):

    crawler = crawlers.Crawler()
    crawler.run()

    return HttpResponse("Crawl success.")
