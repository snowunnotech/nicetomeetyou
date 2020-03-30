#!/usr/bin/env python
import os
import sys
import time
import datetime

import threading




def main(): #Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
def Scrapy():
    Lastcount =0
    while True:
        time.sleep(50)  # 每隔40秒執行一次
        NewCount = Lastcount  # 前一次的數量
        os.system("scrapy crawl udn")
        from chat import models
        Lastcount = models.Udn.objects.all().count()  # 新的數量
        if NewCount!=Lastcount:#若是數量有增加給webSocket訊息
            from chat import consumers
            front = consumers.ChatConsumer
            import asyncio
            loop = asyncio.get_event_loop()
            loop.run_until_complete(front.send_group_msg("front", "ops_coffee","NewNeb"))#傳送訊息
            time.sleep(20)  # 每隔40秒執行一次

if __name__ == "__main__":
    t = threading.Thread(target=Scrapy)
    t.start() #多執行緒 執行Scrapy跟Django Server
    main()


