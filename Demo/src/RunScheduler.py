#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sched 
import time 
import requests
import datetime
import threading

from datetime import datetime,timedelta
from pytz import timezone
import os
def UpdateNews(action_time):
    timeset = 1800
    now_utc = datetime.now(timezone('UTC'))
    now_taipei = now_utc.astimezone(timezone('Asia/Taipei'))
    Now_Time  = now_taipei.strftime(fmt)
    url = 'https://lanmor-py-demo-lanmorop01.c9users.io/UpdateNBANews'
    #os.system("curl -XGET 'https://lanmor-py-demo-lanmorop01.c9users.io/UpdateNBANews'")
    response = requests.get(url)
    scheduler.enterabs(action_time + timeset, 1, UpdateNews, (action_time + timeset,))
    print "UpdateNews_At:%s" % (Now_Time),"=== TimeCycle:%s s" % (timeset)
    
def NotifyRequest(url):
    ##final_url="/{0}/friendly/{1}/url".format(base_url,any_value_here)
    payload = {'number': 2, 'value': 1}
    response = requests.post(url, data=payload)
    
    
#base_url="https://lanmor-bot-lanmor.c9users.io/line-bot/MyApp/"
scheduler = sched.scheduler(time.time, time.sleep) 
fmt = "%Y-%m-%d %H:%M:%S"
now_utc = datetime.now(timezone('UTC'))
now_taipei = now_utc.astimezone(timezone('Asia/Taipei'))
Now_Time  = now_taipei.strftime(fmt)
print 'START:', Now_Time
# 初始化scheduler
scheduler = sched.scheduler(time.time, time.sleep)
# 获得执行调度的初始时间
inittime = time.time()
# 设定调度 使用enterabs设定真实执行时间
# 参数：1 执行时间（time.time格式）2 优先级 3 执行的函数 4 函数参数
scheduler.enterabs(inittime, 1, UpdateNews, (inittime,))
# 执行调度，会一直阻塞在这里，直到函数执行结束
scheduler.run()
