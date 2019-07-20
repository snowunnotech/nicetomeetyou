# Create your views here.
from django.shortcuts import render
from catch.models import Catch
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests,threading
from lxml import etree


# url = 'https://nba.udn.com/nba/index?gr=www'

# Create your views here.
def index(request):
    all = Catch.objects.filter()
    all_title = []
    for i in all:
        all_title.append(i.title)
    return render(request, 'Home/Index.html', {'data': "bt1 ","all_title":all_title})

def content(request):
    content_detail = Catch.objects.filter()

    context = {
        'data': "bt2 ",
        'content_detail': content_detail,
    }
    return render(request, 'Home/Index.html', context)


def search(request):

    url = 'https://nba.udn.com/nba/index?gr=www'
    response = requests.get(url)
    tree = etree.HTML(response.text)
    Data = tree.xpath('//div[@id="mainbar"]/div/div/dl/dt/a')
    address = []
    for i in Data:
        Href = 'https://nba.udn.com/' + i.get('href')  # catch news href
        address.append(Href)
        print('====================================================')
    print('address:', address)
    for x in address:
        url_detail = x
        response_detail = requests.get(url_detail)
        tree_detail = etree.HTML(response_detail.text)
        Data_detail_title = tree_detail.xpath('//div[@id="story_body_content"]/h1')
        Data_detail_text = tree_detail.xpath('//div[@id="story_body_content"]//p')
        Data_detail_time = tree_detail.xpath('//div[@class="shareBar__info--author"]/span')
        Data_detail_pic = tree_detail.xpath('//div[@id="story_body_content"]//img')

        detail_text = ''

        print('address[x]:', x)
        # print('pic:', Data_detail_pic[0].get('data-src'))
        print(Data_detail_time[0].text)
        print(Data_detail_title[0].text)

        for i in Data_detail_text:
            text = i.text
            if text != None:
                detail_text += text
        print('detail_text:', detail_text)
        obj, search_save = Catch.objects.get_or_create(title=str(Data_detail_title[0].text), text=str(detail_text), potime=str(Data_detail_time[0].text),
                            picture=str(Data_detail_pic[0].get('data-src')))
        obj.save()
        if search_save == True:
            newDataCheck = 'T'
        elif search_save == False:
            newDataCheck = 'F'
        print(obj, search_save)
        # search_save = Catch(title=Data_detail_title[0].text, text=detail_text, potime=Data_detail_time[0].text,
        #                     picture=Data_detail_pic[0].get('data-src'))
        # search_save.save()

        # obj, creat = Catch.objects.get_or_create(title='1', text='2', potime='2019-05-16 17:24:00.000000', picture='4')
        # print(obj, creat)
        # obj.save()
    context = {
        'data': "bt3  ",
        'newDataCheck': newDataCheck,
        'pic_src': Data_detail_pic[0].get('data-src'),
    }
    return render(request, 'Home/Index.html', context)


@csrf_exempt
def show(request):
    Area_box = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    json_data = json.dumps(Area_box)
    return HttpResponse(json_data)




