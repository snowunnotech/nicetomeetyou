from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets

from .models import NBA
from .serializers import NewsSerializer
import math

# Create your views here.
def news(request):
    resp = dict()
    total_count = NBA.objects.count()
    total_page = math.ceil(total_count/10)
    page = int(request.GET.get('page', '1'))
    pagination = dict()
    pagination['total_count'] = total_count
    pagination['total_page'] = total_page
    pagination['page'] = page
    resp['meta'] = pagination

    if page < total_page:
        resp['data'] = list(NBA.objects.order_by('-date_time').values()[(page-1)*10:page*10])
    else:
        resp['data'] = list(NBA.objects.order_by('-date_time').values()[(page-1)*10:])

    return JsonResponse(resp)

class NewsViewSet(viewsets.ModelViewSet):
    queryset = NBA.objects.all().order_by('-date_time')
    serializer_class = NewsSerializer