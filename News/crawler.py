from bs4 import BeautifulSoup
import requests


def getNews():
    url = "https://nba.udn.com"
    res = requests.get(url + "/nba/index")
    soup = BeautifulSoup(res.text, 'html.parser')
    news_elements = []

    # 抓取news body dt裡面的資訊
    for news in soup.select("#news_body")[0].select("dt"):
        

        # 抓取title
        title = news.select("h3")[0].text
        # 抓取圖片url
        image_url = news.select("img")[0].attrs.get("src")

        # 抓取內文連結
        content_url = url + news.select("a")[0].attrs.get("href")
        res = requests.get(content_url)
        soup = BeautifulSoup(res.text, 'html.parser')

        content = ""
        for p_label in soup.select("#story_body_content")[0].select("p"):
            if "facebooktwitterpinterest" not in p_label.text:
                content += p_label.text

        news = {
            'title' : title,
            'content' : content,
            'url' : content_url,
            'image_url': image_url
        }

        news_elements.append(news)
    return news_elements