from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import NBAnews
from .serializers import newsSerializer

# Create your views here.

class Get_New_List(APIView):
  def get(self,request):
    news = NBAnews.objects.all()
    serialized = newsSerializer(news,many=True)
    return Response(serialized.data)

def homepage(request):
  news = NBAnews.objects.all()
  context = {'news':news}
  return render(request,'index.html',context)