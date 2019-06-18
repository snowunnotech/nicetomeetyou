from crawler.crawler_NBA import crawler_main
import warnings
from datetime import datetime
import sqlite3


def update_data_to_sqlite():
    warnings.filterwarnings("ignore")
    # 先檢查有最新資料
    conn = sqlite3.connect("./db.sqlite3")
    c = conn.cursor()
    sel = c.execute("select update_time from news order by update_time -1 limit 1")
    conn.commit()
    latest_update = ""
    for data in sel:
        latest_update = data[0]
        # print(latest_update)
    if latest_update == "":
        latest_update = "2019-06-15 00:00"
    conn.close()

    # 依照最新資料去爬
    # default 爬最新的五頁 ~ 最新資料為止

    news = crawler_main(2, latest_update)
    insert_data = []
    print("total:", len(news), "data get")
    for data in news:
        url, title, update_time, content = data
    #     update_time = datetime.strptime(update_time, "%Y-%m-%d %H:%M")
        created = datetime.now().strftime("%Y-%m-%d %H:%M")
        insert_data.append((url, title, update_time, content, created,))

    conn = sqlite3.connect("./db.sqlite3")
    c = conn.cursor()
    c.executemany('INSERT INTO news VALUES (null,?,?,?,?,?)', insert_data)
    conn.commit()
    conn.close()
    # print("data_updated")
