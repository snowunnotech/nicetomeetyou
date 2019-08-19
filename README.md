# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。 **Done**
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。 **Done**
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面： **Done**
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。 **Done**
	
## 進階要求
1. 使用 Scrapy。 **Done**
2. 實現爬蟲自動定時抓取。**Done**
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。
4. 将本 demo 部署至服务器并可正确运行。 **Done**
5. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。
