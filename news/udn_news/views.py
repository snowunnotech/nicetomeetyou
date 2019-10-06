from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers

from .models import TopNews

# from tablib import Dataset
# from import_export import resources
import random
import json


def index(request):
    news_list = TopNews.objects.all()
    context = {
        'news_list': news_list,
    }
    return render(request, 'udn_news/index.html', context)


def getContent(request, id):
    if request.is_ajax():
        ajax_string = 'ajax request: '
    else:
        ajax_string = 'not ajax request: '
    valid_data = TopNews.objects.all().filter(unique_id=id)[0]
    data = HttpResponse(valid_data.data)
    return data
