import os
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)  # 定期執行，每1分鐘執行一次
def cr():
    print('do crawler')
    os.system("python crawler.py")


sched.start()
