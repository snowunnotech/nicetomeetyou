# 項目
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。
	
## 實作方式說明
1. 使用 Scrapy 抓取資料
2. 使用 Django REST Framework 傳遞資料
3. 前端頁面使用AJAX 提取 API 資料。
4. 使用crontab定期運行爬蟲程式爬取資料並儲存至資料庫。
5. 部署至Heroku(url : https://www.slimofy.tk/nba/)
    *使用 Advanced Scheduler   Add-on定時爬蟲