""" This modules contains the test case for Parser"""

import unittest

from crawler.parser import Parser
from crawler.constant import PROJECT_ROOT

class ParserTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_head_news_list(self):
        with open(PROJECT_ROOT + '/crawler/tests/web.html', 'r') as file:
            test_html = file.read()

        news_list = Parser.get_head_news_list(test_html)
        self.assertEqual(4, len(news_list))


    def test_get_new_detail(self):
        reference_title = "穿雷納德球衣「加持」？ 加拿大高球好手抓鳥失利"
        reference_datetime = "2019-06-07 17:36"
        reference_content = "本周開打的PGA加拿大公開賽"
        with open(PROJECT_ROOT + '/crawler/tests/web_detail.html', 'r') as file:
            test_html = file.read()

        title, datetime, content = Parser.get_news_detail(test_html)

        self.assertEqual(reference_title, title)
        self.assertEqual(reference_datetime, datetime)
        self.assertIn(reference_content, content)
