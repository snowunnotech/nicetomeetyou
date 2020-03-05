import time
import os

while True:
    os.system("scrapy crawl news")
    time.sleep(3600)