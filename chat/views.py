# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from rest_framework import viewsets
from .models import Post,Paragraph
from .serializers import ParagraphSerializer,PostSerializer
from django.shortcuts import redirect

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = PostSerializer

def myNBAfeed(request):
    return render(request, 'chat/myNBAfeed.html', {
        'room_name_json': mark_safe(json.dumps("myfeed"))
    })

def removeRec(request):
    Post.objects.all().delete()
    return redirect('/myNBAfeed/')



