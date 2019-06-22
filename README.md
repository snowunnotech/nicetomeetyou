# nice to meet you
V1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。

V2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。

V3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面

V4. 以 Pull-Request 的方式將代碼提交。
	
## 進階要求

V1. 實現爬蟲自動定時抓取。

X2. 每當抓取到新的新聞時立即通知頁面。

V3. 将本 demo 部署至服务器并可正确运行。

目前沒有立即通知頁面  

網站架在GCP上面

http://35.187.144.80:8000/nba_news/
