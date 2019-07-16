from django.test import TestCase

from myproject.core.models import New
from myproject.core.crawler import SimpleCrawler

class CrawlerTest(TestCase):
    def setUp(self):
        pass
        
    def test_crawler(self):
        SimpleCrawler.run()
        
