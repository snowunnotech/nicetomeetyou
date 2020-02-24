from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.
from urllib.request import urlopen
from bs4 import BeautifulSoup
from hotnews.models import nbahotnews

def index(request):

    response = urlopen("https://nba.udn.com/nba/index?gr=www")
    html = BeautifulSoup(response)

    # 抓取焦點新聞清單
    news = html.find("div", class_="box_body")
    news_list = news.find_all("dt")[:-1]
    for lst in news_list:
        n_title = lst.find("h3")
        n_link = "https://nba.udn.com" + lst.find("a")["href"]
        n_intro = lst.find("p")
        n_img = lst.find("img")["src"].replace("200", "292")
        rcd = n_title.text + n_link + n_intro.text + n_img
        print(rcd)

        # 抓取詳細文章
        response_cnt = urlopen(n_link)
        html_cnt = BeautifulSoup(response_cnt)

        # 抓取作者及時間
        cnt_info = html_cnt.find("div", class_="shareBar__info--author")
        n_pubtime = cnt_info.find("span").text
        n_auth = cnt_info.text.split(n_pubtime)[-1]

        # 抓取文章內容
        cnt_box = html_cnt.find("div", id="story_body_content")
        cnt_atcl = cnt_box.find_all("p")[1:]
        n_cnt = "\n".join([aa.text for aa in cnt_atcl])

        print(cnt_info, "\n", n_pubtime, "\n", n_auth, "\n", n_cnt)

        # 存入資料庫
        todb(ntitle=n_title.text, nlink=n_link, nshortcnt=n_intro.text, nimglink=n_img,
             npubtime=n_pubtime, nauth=n_auth, ncontent=n_cnt)

    posts = nbahotnews.objects.all().order_by('-npubtime')

    return render(request, 'hotnews/post_list.html', {'posts': posts})
    # return HttpResponse("Success")

def todb(ntitle, nshortcnt, nlink, nimglink, ncontent='',
         npubtime=timezone.now(), nauth=''):
    try:
        if nbahotnews.objects.get(ntitle=ntitle):
            print("資料重複, 文章標題:", ntitle)
    except:
        unit = nbahotnews(ntitle=ntitle, nlink=nlink, nimglink=nimglink, nshortcnt=nshortcnt, ncontent=ncontent,
                          npubtime=npubtime, nauth=nauth)
        unit.save()
        print("存一筆成功")


