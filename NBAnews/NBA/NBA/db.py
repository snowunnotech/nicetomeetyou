import json
import pymysql

arr = []


def timeStrHandle(time):
    time = "".join(time.split('-'))
    time = "".join(time.split(':'))
    time = "".join(time.split(' '))
    return time


with open('news.json') as f:
    jsonfile = json.loads(f.read())
    for info in jsonfile:
        title = info.get('title')
        content = info.get('content')
        time = info.get('time')
        time = timeStrHandle(time)

        try:

            conn = pymysql.connect(
                host='127.0.0.1', user='root', password='', database='nbanews')
            c = conn.cursor()

            sql = 'SELECT title FROM nba WHERE time = %s' % time

            c.execute((sql))
            check = c.fetchall()
            check = (str(check))

            # str handle  check[3:-5]

            if(check[3:-5] == title):
                print('THIS DATA IS EXISTED')
            else:
                c.execute('INSERT INTO nba(title,content,time) VALUES(%s,%s,%s) ',  (
                    title, content, time))

            conn.commit()
            conn.close()
        except Exception as err:
            print(err)

    # print(str(arr[0])[3:-5])

    f.close()
