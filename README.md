# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。 (O)
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。 (O)
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面： (O)
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。 (O)
	
## 進階要求
1. 使用 Scrapy。 (O)
2. 實現爬蟲自動定時抓取。(X)
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。(X)
4. 将本 demo 部署至服务器并可正确运行。(O)
5. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。(X)

# Source

前後端分離，前端使用Vue搭配express當server、後端使用django、以及Scrapyd server。
- 前端: https://github.com/TsaiWenXue/vue-nba
- 後端: https://github.com/TsaiWenXue/nba
- Scrapy: https://github.com/TsaiWenXue/scrapy

### Deploy on heroku

- [前端](https://vue-nba.herokuapp.com/#/nba-news)

- [後端](https://django-nba.herokuapp.com/news/)

- [Scrapy](https://scrapy-nba.herokuapp.com/)
