""" This modules contains the test case for Scraper """

import unittest

from crawler.scraper import Scraper
from crawler.constant import URL


class ScraperTestCase(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper(URL)
        self.scraper.create_request_headers()
        self.scraper.create_request_data()
        self.scraper.request()
        self.scraper.get_response_text()

    def test_create_request_data(self):

        self.assertTrue(self.scraper.request_data)

    def test_create_request_headers(self):

        self.assertTrue(self.scraper.request_headers)

    def test_request(self):

        self.assertTrue(self.scraper.response)

    def test_get_response_text(self):

        self.assertTrue(self.scraper.text)

        # check get the right content from the web
        self.assertIn("焦點新聞", self.scraper.text)
