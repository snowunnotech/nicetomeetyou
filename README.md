# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
1. 使用 Scrapy。
2. 實現爬蟲自動定時抓取。
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。
4. 将本 demo 部署至服务器并可正确运行。
5. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。

---
# NBA crawler

## Usage
- 進入專案nba_crawler

`cd nba_crawler`

- 創建virtual environment and activate

`python3 -m venv venv`

`source venv/bin/activate`

- 確保之後執行的django server與scrapy爬蟲皆在(venv中)
![](https://i.imgur.com/XXVTrZg.png)

- 安裝所需套件

`pip install django scrapy scrapyd python-scrapyd-api scrapy-djangoitem`

- 進入firstdjango, 執行migration準備資料庫

`cd firstdjango`

`python manage.py makemigrations`

`python manage.py migrate`

![](https://i.imgur.com/Db3GJCu.png)

- 啟動server

`python manage.py runserver`

- 在broser中輸入http://127.0.0.1:8000/ , 進入首頁。

- 目前資料庫為空，因為尚未執行scrapy爬蟲，首頁目前沒有資料

![](https://i.imgur.com/BNCEvbH.png)

- 開啟另一個執行環境(也要先source venv/bin/activate)進入

`/nba_crawler/firstdjango/scrapy_app/scrapy_app`

- 執行一次爬蟲`python main.py`, 此會在網頁中擷取焦點新聞，一次擷取三篇，並用scrapy的pipeline配合Django的model存入DB

- 重新整理首頁，將會多了三筆資料

![](https://i.imgur.com/FUzTYUX.png)

- 每執行一次爬蟲就會多三筆資料
