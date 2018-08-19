from django.shortcuts import render,redirect
import json
from django.http import JsonResponse
from django.http import HttpResponse
from apscheduler.scheduler import Scheduler
from time import sleep
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import os
import re
from django.utils.safestring import mark_safe

from nba.models import get_news,for_button,for_head_line,News

from .serializers import PostSerializer
from rest_framework import viewsets



class api(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = PostSerializer



def log(request):
    if (request):
        headline = for_head_line()
        if(len(headline)>10):

            title= {0:headline[0][0],1:headline[1][0],2:headline[2][0],3:headline[3][0],4:headline[4][0],5:headline[5][0],
                    6: headline[6][0], 7: headline[7][0], 8: headline[8][0], 9: headline[9][0],10: headline[10][0]}
        else:

            title= {0:'notyet',1:'notyet',2:'notyet',3:'notyet',4:'notyet',5:'notyet',
                    6: 'notyet', 7: 'notyet',8: 'notyet', 9: 'notyet',10:'notyet'}
        def task_Fun():

        # # 產生虛擬 borwser：
            service_args = []
            service_args.append('--load-images=no')
            service_args.append('--disk-cache=yes')
            service_args.append('--ignore-ssl-errors=true')
            # DOCKER 虛擬問題 ，依照只是安裝啟動  https://hub.docker.com/r/wernight/phantomjs/
            # driver = webdriver.Remote(command_executor='http://192.168.86.72:8910',desired_capabilities=DesiredCapabilities.PHANTOMJS)  # 位置同浮動ip要改

            driver = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs',
                                          service_args=service_args)
            login_url = 'https://nba.udn.com/nba/cate/6754/'

            driver.get(login_url)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            meta = soup.find_all('a')
            # print(meta)
            count = 0
            http_mark = 'https://nba.udn.com'
            url_list = []
            title_list = []
            for i in meta:  # POST URL ,title
                if i.find('h3'):
                    if i.find('b'):
                        temp_title = i('h3')
                        # print(temp_title)
                        temp_title2 = str(temp_title[0])
                        temp_title2 = temp_title2.split('<h3>')
                        if (temp_title2[0] == ''):
                            count = count + 1
                            temp_title2 = temp_title2[1].split('</h3>')
                            temp_href = i['href']
                            temp_href = http_mark + temp_href
                            url_list.append(temp_href)
                            title_list.append(temp_title2[0])
            for i in range(count):
                print(url_list[i])
                print(title_list[i])
            print('count:{}'.format(count))

            url_content= []
            for i in url_list:
                driver.get(i)
                soup = BeautifulSoup(driver.page_source, "html.parser")
                meta = soup.find_all('p')
                mt = [str(i.text) for i in meta if len(str(i))>7]
                url_content.append(mt)



            pat = re.compile('.*twitter.*')

            new_content= []
            for ii in  url_content:
                a = [i for i in ii if not pat.search(i)]
                new_content.append(a)


            for i in range(count):
                s = ''
                for ii in new_content[i]:
                    s = s + ii
                get_news((title_list[i]), (url_list[i]),s)
                print(s)
                print('')









        sleep(1)

        sched = Scheduler()

        @sched.interval_schedule(seconds=15)
        def my_task1():
            print('爬蟲任務開始\n')
            task_Fun()

            print('爬蟲任務結束\n')

            # @sched.interval_schedule(hours=4)
            # def my_task2():
            #     print('爬蟲任務開始2\n')
            #     sleep(1)
            #     print('爬蟲任務結束2\n')

        sched.start()



        return render(request,'nba/nba.html',locals())

@csrf_exempt
def detail_for_ajax(request):
    # print(for_button())
    a= for_button()
    return JsonResponse({'a':a})



def room(request, room_name):
    return render(request, 'nba/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
