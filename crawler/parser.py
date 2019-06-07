""" This modules contains the class for parser the website """

from bs4 import BeautifulSoup as bs

from crawler.constant import BASE_URL

import pysnooper

class Parser:

    def __init__(self):
        pass

    @staticmethod
    @pysnooper.snoop()
    def get_head_news_list(text):
        news_list = list()
        soup = bs(text, "html.parser")

        news_body = soup.find("div", {"id": "news_body"})
        target_news_list = news_body.findAll("dt")

        for news in target_news_list:
            if news.find("a"):
                news_list.append(BASE_URL + news.find("a")['href'])

        return news_list

    @staticmethod
    def get_news_detail(text):
        raise NotImplementedError
