import requests
from bs4 import BeautifulSoup
import mysql.connector
import pandas as pd
import datetime


# 抓標題etc.
def get_titles(page_count):
    # 標題網址
    url = "https://nba.udn.com/nba/cate/6754/-1/newest/" + str(page_count)

    response = requests.get(url).text
    html = BeautifulSoup(response)
    # 標題
    titles = html.find("div", id="news_list_body").find("dl").find_all("dt")
    return titles


# 抓內容
def get_content(content_url):
    response = requests.get(content_url).text
    html = BeautifulSoup(response)
    # 內容
    content = html.find("div", id="story_body_content").find_all("p")
    rel_date = html.find("div", class_="shareBar__info--author").find("span").text
    content_text = ""
    for data in content:
        if "images" not in data.text.lower():
            content_text += data.text
    # 回傳發布時間,新聞內容
    return rel_date, content_text


def get_mysql_conn():
    # config
    cfg = {
        "host": "nanananana",
        "port": 3306,
        "database": "cv_d_rest",
        "user": "nanananana",
        "password": "nanananana"
    }
    conn = mysql.connector.connect(**cfg)
    return conn


# 匯入mysql
def insert_into_mysql(data_list):
    conn = get_mysql_conn()

    cursor = conn.cursor()
    sql_string = "INSERT INTO nba (title, rel_date, nba_content) VALUES (%s, %s, %s)"

    cursor.executemany(sql_string, data_list)
    conn.commit()

    cursor.close()
    conn.close()


# 從資料庫撈出一筆最新資料做比較是否有更新的,如果有,爬取最新資料
def get_top_news():
    conn = get_mysql_conn()
    df = pd.read_sql("SELECT * FROM `nba` order by rel_date desc limit 1", conn)
    top_rel_date = df["rel_date"][0]
    data_list = crawler_nba_news(top_rel_date)
    return data_list


# 給個時間(datetime),會從最新的抓到給的時間停下(包含)
def crawler_nba_news(end_date):
    data_list = []
    page_count = 0
    while True:
        page_count += 1
        # 當頁資訊
        page_titles = get_titles(page_count)
        # 找不到停下
        if len(page_titles) == 0:
            return data_list
        for data in page_titles:
            # 內容網址
            content_url = "https://nba.udn.com" + data.find("a")["href"]
            # 標題
            title = data.find("h3").text
            # 發布時間,新聞內容
            rel_date_str, text = get_content(content_url)
            rel_date = datetime.datetime.strptime(rel_date_str, '%Y-%m-%d %H:%M')
            if end_date >= rel_date:
                return data_list
            data_list.append([title, rel_date, text])


# 前提要有資料
if __name__ == '__main__':
    # 存csv
    # df = pd.DataFrame(data=data_list, columns=["title", "rel_date", "text"])
    # df.to_csv("./nba_data.csv", encoding="utf8", index=False)

    # 抓取最新資料
    data_list = get_top_news()
    #  如果有最新的,存入mysql
    if len(data_list) > 0:
        insert_into_mysql(data_list)
    # 測試
    # e_date = datetime.datetime(2019, 6, 16, 12, 14)
    # insert_into_mysql(crawler_nba_news(e_date))
