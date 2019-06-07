""" This modules contains the test case for News """

import unittest

from crawler.news import News

class NewsTestCase(unittest.TestCase):
    "Test case for news modules"

    def setUp(self):
        self.news = News()
