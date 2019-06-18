from bs4 import BeautifulSoup
import warnings
import requests
from datetime import datetime
# import pandas as pd


warnings.filterwarnings("ignore")


def crawler_main(pages, newest_update):
    main_url = "https://nba.udn.com/nba/index?gr=www"
    domain_url = "https://nba.udn.com"
    # go to main page > 焦點新聞 more
    newest_update = datetime.strptime(newest_update, "%Y-%m-%d %H:%M")
    url = main_url
    response = requests.get(url)
    html = BeautifulSoup(response.text)
    news_page = domain_url + \
                html.find("div", id="mainbar").find("div", id="news").find("h1", class_="box-title").find("a")["href"]
    # https://nba.udn.com/nba/cate/6754
    # result at 0617
    # news_page = "https://nba.udn.com/nba/cate/6754"
    # go page1_newest
    news_articles = []
    for c_page in range(1, pages + 1):
        url = news_page + "/-1/newest/" + str(c_page)
        response = requests.get(url)
        html = BeautifulSoup(response.text)
        body_box = html.find("div", id="news_list_body").find("dl").find_all("dt")
        b = 0
        for box in body_box:
            url = domain_url + box.find("a")["href"]
            update_time = get_article_update_time(url)
            check_update_time = datetime.strptime(update_time, "%Y-%m-%d %H:%M")
            title = box.find("h3").text
            if check_update_time < newest_update:
                b = 1
                break
            content = get_article_content(url)
            news_articles.append([url, title, update_time, content])
        if b:
            break
    return news_articles


def get_article_update_time(article_url):
    #     article_url = "https://nba.udn.com/nba/story/6780/3877002"
    response = requests.get(article_url)
    html = BeautifulSoup(response.text)
    aritle_update_time = html.find("div", id="shareBar").find("div", class_="shareBar__info") \
        .find("div", class_="shareBar__info--author").find("span").text
    return aritle_update_time


def get_article_content(article_url):
    #     aritle_url = "https://nba.udn.com/nba/story/6780/3877002"
    result = ""
    response = requests.get(article_url)
    html = BeautifulSoup(response.text)
    article_content = html.find("div", id="story_body_content").find_all("p")
    for c in article_content:
        result = result + c.text
    return result


# def main():
#     news = crawler_main(2, "2019-06-17 09:54")
#     df = pd.DataFrame(news, columns=["url", "title", "update_time","content"])
#     print(df)
#
#
# main()
