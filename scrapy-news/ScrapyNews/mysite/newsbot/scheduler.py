# 用來30秒遍歷一次新聞網站的 Scheduler

import time
import os
 
while True:
    os.system("scrapy crawl news")
    time.sleep(30)