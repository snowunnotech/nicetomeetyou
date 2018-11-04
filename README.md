# 徐子函Django

## 環境要求
1. Python 3.6.3
2. Redis

## 運行說明
### 運行於配置好的虛擬環境
若您是以虛擬環境運行本項目，請先修改
"nicetomeetyou/venv/pyvenv.cfg"項下的"home = C:\Users\Lenovo\Anaconda3"，
將"C:\Users\Lenovo\Anaconda3"改為您正式安裝的Python解釋器所在的地址
1. 運行Redis，保證端口號為6379
2. 運行本項目，預留8000端口
3. 運行命令 <本項目地址>/venv/Scripts/python <您項目地址>/manage.py runserver
### 直接運行
請先確定您是否安裝本項目所使用的第三方庫，若您已經安裝，則可直接於您的
Python環境下運行本項目，而下面是運行步驟:
1. 運行Redis，保證端口號為6379
2. 運行本項目，預留8000端口
3. 運行命令 python <您項目地址>manage.py runserver

## 爬蟲說明
### 運行於配置好的虛擬環境
若您要直接使用爬蟲，請運行
<您項目地址>/venv/Scripts/python <您項目地址>/crawler/crawler_starter.py
### 直接運行
python <您項目地址>/crawler/crawler_starter.py

## 使用的Python第三方庫
1. Automat=0.7.0
2. Click=7.0
3. Django=2.1.2
4. Flask=0.11.1
5. Flask-RESTful=0.3.6
6. Flask-Uploads=0.2.1
7. Jinja2=2.10
8. MarkupSafe=1.0
9. PyHamcrest=1.9.0
10. Twisted=18.9.0
11. Werkzeug=0.14.1
12. aioredis=1.2.0
13. aniso8601=4.0.1
14. asgiref=2.3.2
15. async-timeout=3.0.1	
16. attrs=18.2.0
17. autobahn=18.10.1
18. beautifulsoup4=4.6.3
19. bs4=0.0.1
20. certifi=2018.10.15
21. chardet=3.0.4
22. constantly=15.1.0
23. daphne=2.2.2
24. django-crontab=0.7.1
25. django-model-utils=3.1.2
26. django-notifications-hq=1.5.0
27. django-redis=4.9.0
28. hiredis=0.2.0
29. hyperlink=18.0.0
30. idna=2.7
31. incremental=17.5.0
32. itsdangerous=1.1.0
33. jieba=0.39
34. jsonfield=2.0.2
35. lxml=4.2.5
36. msgpack=0.5.6
37. numpy=1.13.1
38. pandas=0.23.4
39. pbr=3.1.1
40. pip=10.0.1
41 py2neo=3.1.2
42. pypinyin=0.22.0
43. python-dateutil=2.7.5
44. pytz=2018.7
45. pywin32	224	224
46. redis=2.10.6
47. requests=2.12.1
48. setuptools=39.1.0
49. six=1.11.0
50. txaio=18.8.1
51. urllib3=1.24
52. xlrd=1.0.0
53. xlwt=1.2.0
54. zope.interface=4.6.0

## 視圖接口說明
### 查看新聞列表
#### API樣例
http://127.0.0.1:8000/news_list/
#### 方法
GET
#### 變量
無
#### 返回樣例
網頁視圖

### 查看特定ID新聞
#### API樣例
http://127.0.0.1:8000/get_news/id=<newsId>
#### 方法
GET
#### 變量
1. id: 欲查詢的新聞ID
#### 返回樣例
網頁視圖

## 接口說明
### 以給定的新聞ID查看新聞
#### API樣例
http://127.0.0.1:8000/get_news_by_id/id=<newsId>
#### 方法
GET
#### 變量
1. id: 欲查詢的新聞ID
#### 返回值變量
{
    "id": 1,
    "title": "測試報導1",
    "author": "測試記者報導1",
    "content": "測試新聞內容1",
    "news_url": "https://nba.udn.com/test/test/1/",
    "org_news_date": "2018-11-01T12:30:00Z",
    "created_date": "2018-11-02 03:02:57"
}

### 引入新聞
http://127.0.0.1:8000/import_news/
#### 方法
POST
#### 變量
1. news_json: 轉換為json的新聞
#### 回傳樣例
{
    'msg': '成功'
}

### 實時加載最新引入的新聞
http://127.0.0.1:8000/get_newsfeed/
####方法
GET
#### 變量
無
#### 返回值樣例
{
    "data": [
        {
            "id": 1,
            "title": "測試報導1",
            "author": "測試記者報導1",
            "content": "測試新聞內容1",
            "news_url": "https://nba.udn.com/test/test/1/",
            "org_news_date": "2018-11-04 11:25",
            "created_date": "2018-11-04 03:29:28"
        },
        {
            "id": 2,
            "title": "測試報導2",
            "author": "測試記者報導2",
            "content": "測試新聞內容2",
            "news_url": "https://nba.udn.com/test/test/2/",
            "org_news_date": "2018-11-04 10:32",
            "created_date": "2018-11-04 03:29:30"
        }
    ]
}
### 加載新聞(前端datatables插件使用)
http://127.0.0.1:8000/get_news_for_table_data/
#### 方法
POST
#### 變量
1. draw: 避免XSS攻擊的變量
2. start: 從start記錄開始
3. length: 欲查詢紀錄的長度
#### 返回值樣例
{
    "draw": 0,
    "recordsTotal": 60,
    "recordsFiltered": 60,
    "data": [
        {
            "id": 1,
            "title": "測試報導1",
            "author": "測試記者報導1",
            "content": "測試新聞內容1",
            "news_url": "https://nba.udn.com/test/test/1/",
            "org_news_date": "2018-11-01T15:29:00Z",
            "created_date": "2018-11-02 03:02:52"
        },
        {
            "id": 2,
            "title": "測試報導2",
            "author": "測試記者報導2",
            "content": "測試新聞內容2",
            "news_url": "https://nba.udn.com/test/test/2/",
            "org_news_date": "2018-11-01T14:27:00Z",
            "created_date": "2018-11-02 03:02:53"
        }
    ]
}

## 自動排程功能
### 運行於配置好的虛擬環境
運行命令 <本項目地址>/venv/Scripts/python <您項目地址>/manage.py crontab add 
### 直接運行
運行命令 python <您項目地址>/manage.py crontab add 
### 其他說明
只有Linux操作系統才支持排程功能，若您成功運行了排程，會於每10分鐘運行1次爬蟲

# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
1. 實現爬蟲自動定時抓取。
2. 每當抓取到新的新聞時立即通知頁面。
3. 将本 demo 部署至服务器并可正确运行。