from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post
import requests
import re
from bs4 import BeautifulSoup

def hello_world(request):
    return render(request, 'nba_template.html', {'current_time': str(datetime.now()),})

def home(request):
    crawl_web(request)
    nba_list = Post.objects.all()
    nba = {
    "nba": nba_list
    }
    return render(request, 'home.html', nba)


def crawl_web(request):
    url='https://nba.udn.com/nba/index?gr=www'
    target_urls = []
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    content = s.findAll('div', {'id':re.compile('^news_body')})[0].contents[0].contents
    index = 0
    equal = 0
    for i in content:
        print(i)
        print('\n')
    while True:
        try:
            cont = content[index]
            # print(content[index])
            cont = str(cont).split('<h3>')[1].split('</h3><p>')
            
            index += 1
            if Post.objects.count() == 0:
                new_nba = Post.objects.create(title=cont[0], content=cont[1].split('...')[0])
                break
            for i in range(Post.objects.count()):
                if cont[0] != Post.objects.all()[i].title:
                    equal += 1
            if equal == Post.objects.count():
                new_nba = Post.objects.create(title=cont[0], content=cont[1].split('...')[0])
                equal = 0
        except:
            index += 1
            break
    nba_list = Post.objects.all()
    nba = {
    "nba": nba_list
    }
    return render(request, 'home.html', nba)
# print(crawl_web('https://nba.udn.com/nba/index?gr=www'))
