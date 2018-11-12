# nice to meet you
1. - [x] 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. - [x] 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. - [x] 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. - [x] 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
1. - [x] 實現爬蟲自動定時抓取。
	- 以ajax送request到爬蟲的function，設定setInterval的時間，定時抓取資料
2. - [ ] 每當抓取到新的新聞時立即通知頁面。
3. - [x] 将本 demo 部署至服务器并可正确运行。
	- 將Django+uWSGI+Nginx+Ubuntu部屬到 AWS EC2主機上
	- [網址](http://18.237.6.104/news/) : http://18.237.6.104/news/ (設定抓取時間為一小時)
