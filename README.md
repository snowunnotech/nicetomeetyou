# nice to meet you [ALL Done]
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
[由於佈署在heroku上，因此定時抓取改用js function達成，而原本則為django-crontab]
[https://nicetomeetyouwcc.herokuapp.com/nba_news_list]
