import pymongo
import pandas as pd
import numpy as np
from crawler.crawler_NBA import crawler_main
from datetime import datetime


def main():
    # get newest data from mongodb
    client = pymongo.MongoClient()
    ChuangShun_tech = client.ChuangShun_tech
    NBA_new = ChuangShun_tech.NBA_new
    # NBA_new.drop()
    try:
        lastest_update = NBA_new.find().sort("update_time", -1)[0]["update_time"]
        lastest_update = datetime.strftime(lastest_update, "%Y-%m-%d %H:%M")
        #     if no data on database
    except IndexError:
        print("no_old_data")
        lastest_update = "2019-06-10 00:00"
    news = crawler_main(3, lastest_update)
    df = pd.DataFrame(news, columns=["url", "title", "update_time", "content"])
    arr = np.array(df)
    print("crawler_done")
    for i in range(len(arr)):
        url, title, update_time, content = arr[i, :]
        update_time = datetime.strptime(update_time, "%Y-%m-%d %H:%M")
        update_data = {"url": url, "title": title, "update_time":update_time, "content": content}
        NBA_new.update_one({"url": url}, {"$set": update_data}, upsert=True)
    print("update_done")

    # result = NBA_new.find().limit(5)
    # for data in result:
    #     print(data)


main()
