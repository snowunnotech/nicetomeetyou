from django.shortcuts import render, HttpResponse
import InitRun
# from .tasks import InitRun
import time

# Create your views here.
def celeryTask(request):
    InitRun.Run()
    return HttpResponse('done')