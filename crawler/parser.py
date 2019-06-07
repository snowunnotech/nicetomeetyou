""" This modules contains the class for parser the website """

from bs4 import BeautifulSoup as bs

from crawler.constant import BASE_URL


class Parser:
    "Parser for news list and news detail"

    def __init__(self):
        pass

    @staticmethod
    def get_head_news_list(text):
        "Get head news list"
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
        "Get news detail like title, datetime, and content"
        soup = bs(text, "html.parser")
        paragraph_list = list()

        story_body = soup.find("div", {"id": "story_body_content"})

        title = story_body.find("h1").text

        datetime_str = story_body.find("div", {
            "class": "shareBar__info--author"
        }).find("span").text

        target_paragraph_list = story_body.findAll("p")
        for paragraph in target_paragraph_list:
            if paragraph.text:
                paragraph_list.append(paragraph.text)
        content = "".join(paragraph_list)

        return title, datetime_str, content
