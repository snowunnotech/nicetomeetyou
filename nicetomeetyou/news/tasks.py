from . crawlers import Crawler


def news_crawler():
    crawler = Crawler()
    crawler.run()
