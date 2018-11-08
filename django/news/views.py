from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import News
from .serializers import NewsSerializer


class NewsView(APIView):

    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        news = serializer.data
        return Response(news, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsDetail(APIView):

    def get_object(self, pk):
        try:
            return News.objects.get(pk=pk)
        except News.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        news = self.get_object(pk)
        serializer = NewsSerializer(news)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        news = self.get_object(pk)
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        news = self.get_object(pk)
        news.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    return render(request, "news/index.html", locals())


def show_detail(request, *args, **kwargs):
    return render(request, "news/detail.html", locals())
