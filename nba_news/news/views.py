from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import News
import requests
from .crawl import crawl_news, save
from django.core import serializers

def renew_data():
    del_data()
    url = 'https://nba.udn.com/nba/index?gr=www '
    latest_news = crawl_news(url)
    save(latest_news)
    print(latest_news)
    # News.objects.create(content='adfsdf', title='asdfghjk')
    # return HttpResponse("Hello world")

def del_data():
    News.objects.all().delete()

    
def get_news(request):
    if request.is_ajax() and request.method == 'POST':
        all_data = News.objects.all()
        print('getting news')
        # print(all_data)
        title = [data.title for data in News.objects.all()]
        content = [data.content for data in News.objects.all()]
        img = [data.img_url for data in News.objects.all()]
        url = [data.page_url for data in News.objects.all()]
        # print(title, type(title))


        all_data = list(zip(title, content, img, url))

        
        # return HttpResponse(all_data)
        return JsonResponse({'news': all_data})


def show_page(request):
    renew_data()
    # all_data = News.objects.all()[0]
    # print(all_data)
    # all_data = [data.title for data in News.objects.all()]
    # return HttpResponse(all_data)
    return render(request, 'index.html')
    # return render(request, 'index.html', {'data': all_data})


# Create your views here.
