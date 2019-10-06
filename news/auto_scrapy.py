import time
import os
import sched
from subprocess import Popen

schedule = sched.scheduler(time.time, time.sleep)


def func():
    # Popen("cd D:\DjangoEnv\\nicetomeetyou\\news\\bots\\top_news_bot")
    Popen("curl http://localhost:6800/schedule.json -d project=top_news_bot -d spider=top_news_spider")

    # os.system("scrapy crawl News")


def perform1(inc):
    schedule.enter(inc, 0, perform1, (inc,))
    func()


def mymain():
    schedule.enter(0, 0, perform1, (180,))


if __name__ == "__main__":
    mymain()
    schedule.run()
