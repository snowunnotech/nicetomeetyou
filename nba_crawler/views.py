from .models import News
from .serializers import NewsSerializer
from django.template.loader import get_template
from django.http import HttpResponse
from rest_framework import viewsets


# Create your views here.
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

def NewsListView(request):
    return HttpResponse(get_template('list.html').render())

def NewsDetailView(request, n):
    return HttpResponse(get_template('detail.html').render({'n':n}))