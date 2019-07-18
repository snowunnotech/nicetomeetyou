import sys
sys.path.append('Spider')
import scrapy
from scrapy.settings import Settings
from FullSpider import settings as my_settings
from scrapy.crawler import CrawlerProcess

crawler_settings = Settings()
crawler_settings.setmodule(my_settings)
def run_scrapy(ob_scr):
	c = CrawlerProcess(
	    settings=crawler_settings
	)
	c.crawl(ob_scr)
	c.start()