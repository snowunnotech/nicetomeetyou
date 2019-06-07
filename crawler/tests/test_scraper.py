""" This modules contains the test case for Scraper """

import unittest

from crawler.scraper import Scraper
from crawler.constant import BASE_URL, TEST_URL, PROJECT_ROOT


class ScraperTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_scraper(self):
        '''
        test for scrap for website
        '''
        self.scraper = Scraper(BASE_URL)
        self.scraper.create_request_headers()
        self.scraper.create_request_data()
        self.scraper.request()
        self.scraper.get_response_text()

        hot_news = "焦點新聞"

        self.assertTrue(self.scraper.request_data)
        self.assertTrue(self.scraper.request_headers)
        self.assertTrue(self.scraper.response)
        self.assertTrue(self.scraper.text)
        # check get the right content from the web
        self.assertIn(hot_news, self.scraper.text)

    def test_get_response_text_of_news_detail(self):
        '''
        test for scrap for detail website
        '''
        self.scraper = Scraper(TEST_URL)
        self.scraper.create_request_headers()
        self.scraper.create_request_data()
        self.scraper.request()
        self.scraper.get_response_text()

        news_title = "穿雷納德球衣「加持」？ 加拿大高球好手抓鳥失利"

        self.assertIn(news_title, self.scraper.text)
