# nice to meet you
- [X] 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
- [X] 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
- [X] 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
- [X] 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
- [X] 使用 Scrapy。
- [ ] 實現爬蟲自動定時抓取。
- [ ] 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。
- [X] 将本 demo 部署至服务器并可正确运行 - [伺服器](http://140.138.150.47:8000/showNews/)。
- [ ] 所實現新聞列表 API 可承受 100 QPS 的壓力測試。

**Please put the config.py to the root dir**

config.py

```python
host = "ypur server"
user = "user name in MySQL"
password = "password in MySQL"
db = "DB's name"
```

