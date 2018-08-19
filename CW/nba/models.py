from django.db import models,connection
import MySQLdb

class News(models.Model):
    title = models.CharField(max_length=200, blank=True,unique=True)
    link = models.CharField(max_length=200, blank=True)
    content= models.TextField(max_length=20000, blank=True)

    class Meta:
        db_table = "News"




def get_news(t,l,c):
    with connection.cursor() as cursor:
        # cursor.execute("alter table News modify title MEDIUMTEXT character set utf8")  # 存入中文要先轉換utf8  MEDIUMTEXT:最多可以存到16mb長度
        # cursor.execute("alter table News modify link MEDIUMTEXT character set utf8")

        # cursor.execute("alter DATABASE nba_mysql CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")
        cursor.execute("alter table News CONVERT TO CHARACTER SET utf8")
        cursor.execute("alter table News modify content MEDIUMTEXT character set utf8")
        cursor.execute('insert into News(title,link,content) values ("{}","{}","{}") on duplicate key update title ="{}" '.format(t,l,c,t) )


  #再來確認資料數據是否重複
        # 第三步：reverse 資料 最新的擺前面輸出
    cursor.close()
    return


def for_head_line():
    with connection.cursor() as cursor:
        cursor.execute("select title from News")
        cc = [c for c in cursor.fetchall()]

    cursor.close()
    return cc

def for_button():
    with connection.cursor() as cursor:
        cursor.execute("select content from News")
        cc = [c for c in cursor.fetchall()]


    cursor.close()
    return cc