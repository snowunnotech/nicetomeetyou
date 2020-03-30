from django.shortcuts import render
from django.shortcuts import render
from django import template
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.http import HttpResponse
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
from urllib import request, parse
import os
import time
import lxml.html
import re
import urllib.parse
import pandas as pd
import numpy as np
import csv
import jieba
import pymysql
import random
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.urls import reverse
from .models import Udn
from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.views.generic import View
import time
import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Udn
from .serializers import UdnSerializer
def chat(request):#首頁邏輯
    global PageGlobal
    PageGlobal=2
    JsonDict = Udn.objects.all().order_by('-time')[:20].values("title","link","time")#起始20篇
    return render(request, 'chat.html',locals())
class UdnViewSet(viewsets.ModelViewSet):
    queryset = Udn.objects.all()
    serializer_class = UdnSerializer

def index_Ajax(request):
    global PageGlobal
    ArticleCount=PageGlobal #用全域變數紀錄接下來顯示的新文數
    AjAxJsonDict = list(Udn.objects.all().order_by('-time')[(ArticleCount*10):(ArticleCount*10+10)].values("title", "link", "time"))#一次十篇
    PageGlobal+=1
    return JsonResponse(AjAxJsonDict, safe=False)
def post_record(request,title):
    Title=title
    global PageGlobal
    PageGlobal=2
    ArticleCount=PageGlobal
    PostJsonDict = Udn.objects.all().order_by('-time')[(ArticleCount):(ArticleCount +20)].values("title", "link", "time")
    return render(request,'post_record.html',locals())