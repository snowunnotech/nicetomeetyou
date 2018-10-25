from django.shortcuts import render
from django.contrib.auth.models import User, Group
from news.models import newscatch
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from news.serializers import newscatchSerializer
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.

class Get_nbanew(APIView):
    def get(self, request):
        news = newscatch.objects.all()
        serializer_class = newscatchSerializer(news, many=True)
        return Response(serializer_class.data)

def newspage(request):
    template = get_template('news_page.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(context = locals(),request=request)
    return HttpResponse(html)