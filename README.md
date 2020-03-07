#目前：
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 實現爬蟲自動定時抓取。(每 1 分鐘進行一次抓取，目前設定為抓取3頁，不過變數可調整)

#未來目標：
1. 使用 Scrapy。
2. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。
3. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。
