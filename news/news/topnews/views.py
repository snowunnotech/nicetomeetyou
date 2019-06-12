import datetime

from rest_framework import viewsets
from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import News
from .serializers import NewsSerializer
from . import crawler

# Show data from database by viewset
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Home page
def homepage(request):

    # Re-crawl when has passed 1 hour or hasn't crawl yet
    # We don't have to crawl every time refresh homepage in order to save time
    if not(News.objects.get(id=1).crawl_time) or (timezone.now() - News.objects.get(id=1).crawl_time > datetime.timedelta(hours=1)):
        crawl_data()

    return render(request, 'index.html')

# Show detail of each news
class NewsDetailView(generic.DetailView):
    model = News

# Crawl data and put it in "News" model
def crawl_data():

    # Web-crawler program
    result = crawler.get_data()

    # Put ten top news in database
    for i in range(10):
        
        # If data existed, update it
        if News.objects.filter(id=i+1):

            News.objects.filter(id=i+1).update(
                link = result['link'][i],
                pre_img_link = result['pre_img_link'][i],
                title = result['title'][i],
                time = result['time'][i],
                preview = result['preview'][i],
                img_link = result['img_link'][i],
                paragraph = result['paragraph'][i],
                crawl_time = timezone.now(),
            )
        # If data is not existed, create a new one
        else:
            News.objects.create(
                link = result['link'][i],
                pre_img_link = result['pre_img_link'][i],
                title = result['title'][i],
                time = result['time'][i],
                preview = result['preview'][i],
                img_link = result['img_link'][i],
                paragraph = result['paragraph'][i],
                crawl_time = timezone.now(),
            )