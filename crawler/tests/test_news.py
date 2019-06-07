""" This modules contains the test case for News """

import unittest

from crawler.news import News

class NewsTestCase(unittest.TestCase):

    def setUp(self):
        self.news = News()

    def test_get_news_detail(self):
        raise NotImplementedError
