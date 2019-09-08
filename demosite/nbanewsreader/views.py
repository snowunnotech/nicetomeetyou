from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })