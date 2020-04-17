from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def start_crawler():
    settings = get_project_settings()
    settings.update({'SPIDER_MODULES': 'crawler.crawler.spiders',
                     'ITEM_PIPELINES': {'crawler.crawler.pipelines.CrawlerPipeline': 300}
                     })

    process = CrawlerProcess(settings)
    process.crawl('nba_news_crawler')
    process.start()


if __name__ == "__main__":
    start_crawler()
