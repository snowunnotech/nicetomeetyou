import re
import time
import requests
from bs4 import BeautifulSoup
from django.core.exceptions import ObjectDoesNotExist
from news.models import News


def getTotalPage(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "html.parser")
        total = int(re.findall(
            r"[0-9]+", str(soup.findAll('span', 'total')))[0])
    return total


def checkNewsInDb(_id):
    try:
        a = News.objects.get(uuid=_id)
        return True
    except ObjectDoesNotExist:
        return False


def getUrlList():
    total_page = getTotalPage("https://nba.udn.com/nba/cate/6754/-1/newest/1")
    base_url_iter = "https://nba.udn.com/nba/cate/6754/-1/newest/{0}"

    href_list = []
    index = 1
    while index < total_page:
        r = requests.get(base_url_iter.format(index))
        if r.status_code == requests.codes.ok:
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, "html.parser")
            news = soup.find('div', id='news_list_body')

            href_list.extend(["https://nba.udn.com/" + each.get('href')
                              for each in news.findAll('a')])
        time.sleep(1)
        index += 1
    return href_list


def getNewsContent():
    href_list = getUrlList()

    for each in href_list:
        print(each)
        _id = each.split('/')[7]
        r = requests.get(each)
        if r.status_code == requests.codes.ok:
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, "html.parser")
            title = soup.select('#story_body_content > h1')[0].text
            date = soup.select(
                '#shareBar > div.shareBar__info > div > span')[0].text
            text_list = soup.select('#story_body_content > span > p')

            text = ''
            for i in range(len(text_list)):
                if i == 0:
                    pass
                elif text_list[i].text:
                    text += text_list[i].text

            if not checkNewsInDb(_id):
                n = News.objects.create(
                    uuid=_id, title=title, published_date=date, text=text)
                n.save()
        time.sleep(1)
