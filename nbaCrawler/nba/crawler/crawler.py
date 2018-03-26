from bs4 import BeautifulSoup
from nba.models import News
import requests

url = "https://nba.udn.com"

res = requests.get(url + "/nba/index?gr=www")

soup = BeautifulSoup(res.text, 'html.parser')

for news in soup.select("#news_body")[0].select("dt"):
    title = news.select("h3")[0].text
    content_url = url + news.select("a")[0].attrs.get("href")

    res = requests.get(content_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    content = ""
    for p in soup.select("#story_body_content")[0].select("p"):
        if "facebooktwitterpinterest" not in p.text:
            content += p.text

    print(title)
    print(content)
    print(content_url)
