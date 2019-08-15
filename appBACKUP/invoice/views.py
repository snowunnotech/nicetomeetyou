import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import requests
from helper.helper import APIHandler
import logging

from invoice.services import *

# Get an instance of a logger
logger = logging.getLogger('django.request')

# set variables
public_url = os.getenv('public_url')
public_url_sendmail = os.getenv('public_url_sendmail')

# Create invoice via ezpay
# 開一個invoice紀錄的table, 一旦有創建或修改刪除就記錄下來（？），一樣需要同步從ezpay查到的發票紀錄
class CreateB2CInvoice(APIView):
    def post(self, request):
        data = request.data
        print ('data', data)
        response = CREATE_B2C_CREDITCARD_INVOICE(data)
        response = json.loads(response.content)
        return APIHandler.catch(data=response, code='000')