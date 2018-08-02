from django.shortcuts import render, HttpResponse

from .tasks import runspider


def celeryTask(request):
    runspider.delay()
    return HttpResponse('ok')
