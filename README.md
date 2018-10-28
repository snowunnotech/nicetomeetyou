# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。  [完成]
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。  [完成]
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：OK!
	 * 焦點新聞列表 [完成]
	 * 新聞詳情頁面 [完成]
4. 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
1. 實現爬蟲自動定時抓取。 
   [完成][利用Django Q設定完成，每十分鐘抓取一次]
2. 每當抓取到新的新聞時立即通知頁面。
   [完成][利用資料庫長度去辨識，若裡面將跳視窗通知。]
3. 将本 demo 部署至服务器并可正确运行。
   [完成][linode有租一個小空間網址為：http://172.104.66.171/news/]

   發布部署與本地端部署有些維權線上差異