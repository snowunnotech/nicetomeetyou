from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
import time
import NewsSpider.settings
import os

class UdnnbanewsparserConfig(AppConfig):
	name = 'UdnNBANewsParser'
	crawl_time = 0

	def ready(self):
		if 'IS_SCRAPY' in os.environ:
			return
		self.auto_crawl()
		scheduler = BackgroundScheduler()
		scheduler.add_job(self.auto_crawl, 'interval', minutes=10)
		scheduler.start()

	def auto_crawl(self):
		cwd = NewsSpider.settings.BASE_DIR + '/nbaBot/nbaBot/spiders'
		subprocess.Popen(['scrapy', 'runspider', 'udn_spider.py'], cwd=cwd)
		print("auto_crawl", self.crawl_time)
		self.crawl_time += 1