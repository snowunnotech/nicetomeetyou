from django.http import HttpResponse
from datetime import datetime

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import NbaNewsSerializer
def hello_django(request):
    return HttpResponse("Hello django!")

class get_news_List(APIView):
    def get(self, request):
        news = Post.objects.all()
        serialized = NbaNewsSerializer(news, many=True)
        return Response(serialized.data)

# Create your views here.
def hello_django(request):
    return render(request, 'hello_django.html', {
        'current_time' : str(datetime.now()),
    })

def topnba(request):
    nba_list = Post.objects.all()
    return render(request, 'topnba.html', {
        'nbalist' : nba_list,
    })

# class nbanews(generic.DateDetailView):
#     model = Post
#     template_name =r'..\templates\hello_django.html'
#
# def append(request):
#     new_post = Post(post=request.get['title'])