import os
import time
import sched

schedule = sched.scheduler(time.time, time.sleep)

def RunScrapy():
	os.system('scrapy crawl nba')

def SetNext(delaytime):
	RunScrapy()
	schedule.enter(delaytime, 1, SetNext, (90,))

def main():
	schedule.enter(0, 1, SetNext, (90,))

if __name__ == "__main__":
	main()
	schedule.run()