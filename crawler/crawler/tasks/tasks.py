# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from crawler.crawler.spiders.news_spider import NewsSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


@shared_task
def crawl():
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    d = runner.crawl(NewsSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished

@shared_task
def justsaysomething():
    print('************I want a job...******************')

@shared_task
def crawler_job():
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(NewsSpider)
    process.start()