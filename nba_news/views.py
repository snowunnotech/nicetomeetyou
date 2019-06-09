from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News
from .serializers import newsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions



class GetNewsList(APIView):
    def get(self, request):
        news = News.objects.all().order_by('-id')
        serialized = newsSerializer(news, many=True)
        return Response(serialized.data)

class GetNewsDetail(APIView):
    def get(self, request, idd):
        data = News.objects.filter(id=idd)
        serialized = newsSerializer(data, many=True)
        return Response(serialized.data)


def homepage(request):
    return render(request, 'index.html')

def detail(request, id):
    data = get_object_or_404(News, id = id)
    return render(request, 'detail.html', {'data':data})
