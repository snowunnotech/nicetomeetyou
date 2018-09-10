from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FocusNew
from .serializers import FocusNewSerializers

# Create your views here.
class GetFocusNewList(APIView):
    def get(self, request):
        focusnew = FocusNew.objects.all()
        serialized = FocusNewSerializers(focusnew, many=True)
        return Response(serialized.data)

def hello(request):
    return render(request, 'focusnew_list.html')

