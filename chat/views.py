# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json



def myNBAfeed(request):
    return render(request, 'chat/myNBAfeed.html', {
        'room_name_json': mark_safe(json.dumps("myfeed"))
    })