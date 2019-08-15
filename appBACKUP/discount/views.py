import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from helper.helper import APIHandler
from .services import *

import sentry_sdk
sentry_url = os.getenv('SENTRY_URL')
sentry_sdk.init(sentry_url)
# Create your views here.

class Activate_Topex_Customer(APIView):
    def get(self, request):
        info_list = GET_ALL_TOPEX_MEMBER()
        return APIHandler.catch(data=info_list, code='BA1')

    def put(self, request):
        customer_id = request.data.get('customer_id')
        quota = request.data.get('quota')
        update_status = CHANGE_TOPEX_QUOTA(customer_id, quota)
        return APIHandler.catch(data={"topex_id":update_status}, code='BA3')

    def post(self, request):
        customer_id = request.data.get('customer_id')
        update_status = ACTIVATE_TOPEX_CUSTOMER(customer_id)
        return APIHandler.catch(data={"topex_id":update_status}, code='BA0')

    def delete(self, request):
        customer_id = request.data.get('customer_id')
        update_status = REMOVE_TOPEX_CUSTOMER(customer_id)
        return APIHandler.catch(data={"topex_id":update_status}, code='BA2')

class Ecredit_Amount(APIView):
    def post(self, request):
        change_point = request.data.get('change_point')
        add_minus = request.data.get('add_minus')
        description = request.data.get('description', '')
        customer_id = request.data.get('customer_id')
        price_prefix = request.data.get('price_prefix', '')
        transaction_id = request.data.get('transaction_id')
        ECREDIT_VALUE_CONTROL(customer_id, change_point, add_minus, price_prefix, transaction_id, description)
        return APIHandler.catch(data='Success', code='000')

