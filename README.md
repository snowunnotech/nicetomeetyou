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

## 答題說明
* 使用`requests`抓取資料
* 使用 Django REST Framework 傳遞資料
* 前端頁面使用AJAX
* 使用crontab定期運行爬蟲程式爬取資料並儲存至資料庫
* 部署至Heroku上: https://crawlnba.herokuapp.com/
