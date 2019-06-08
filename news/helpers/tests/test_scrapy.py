""" This test case is for news helper scrapy """
from django.test import TestCase

from datetime import datetime

from faker import Factory

from core.constant import INDEX_URL, TEST_URL, PROJECT_ROOT

from news.helpers.scrapy import CrawlerService
from news.models import News


faker = Factory.create()

class CrawlerServiceTestCase(TestCase):

    def setUp(self):
        pass

    def test_request_head_news_list(self):
        reference_news_list_len = 3

        crawler_service = CrawlerService(INDEX_URL)
        news_list = crawler_service.request_head_news_list()

        self.assertEqual(reference_news_list_len, len(news_list))

    def test_request_news(self):
        reference_title = "穿雷納德球衣「加持」？ 加拿大高球好手抓鳥失利"
        crawler_service = CrawlerService()
        news = crawler_service.request_news(TEST_URL)

        test_news = News.objects.filter(title=reference_title).first()

        self.assertIsNotNone(test_news)

    def test_get_news(self):
        reference_news_list_len = 3
        crawler_service = CrawlerService(INDEX_URL)

        news_url_list = crawler_service.request_head_news_list()
        news_list = crawler_service.get_news()
        self.assertEqual(reference_news_list_len, len(news_list))

    def test_run(self):
        reference_news_list_len = 3

        crawler_service = CrawlerService(INDEX_URL)
        crawler_service.run()

        test_news_list = News.objects.all()

        self.assertEqual(reference_news_list_len, len(test_news_list))
