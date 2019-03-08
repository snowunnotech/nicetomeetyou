# nice to meet you
1. （完成） 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. （完成）使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. （完成）使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. （完成）以 Pull-Request 的方式將代碼提交。
	
## 進階要求
1.（完成）實現爬蟲自動定時抓取。
* 使用 Heroku scheduler 做排程，目前是10分鐘執行一次爬蟲 
    
2.（完成）每當抓取到新的新聞時立即通知頁面。
* 使用web notify 通知，要訂閱允許才可以使用。如果有新的資料會通知所有使用者  
    
3.（完成）将本 demo 部署至服务器并可正确运行。
* 已部署至Heroku 雲端平台
* 連結：[https://nbanewsdemo.herokuapp.com/](https://nbanewsdemo.herokuapp.com/)
   

### 其他

model

News: 是存新聞資料，未來可以增加欄位

PushToken: 存使用者的訂閱token 

爬蟲程式：放在 crawler

可爬取其他分頁，後面給參數
* 第一個參數：爬第幾頁 default = 1
* 第二個參數：爬到幾頁 default = 1

Ex. python -m crawler.crawlerNewsList 1 5


  