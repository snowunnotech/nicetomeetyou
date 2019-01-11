# nice to meet you
- [x] 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。 
- [x] 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，並將所抓取新聞存儲至 DB。
- [x] 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 - [x] 焦點新聞列表
	 - [x] 新聞詳情頁面
- [x] 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
- [x] 實現爬蟲自動定時抓取。    
Use schelduler from Heroku
- [x] 每當抓取到新的新聞時立即通知頁面。
- [x] 將本 demo 部署至伺服器並可正確運行。   
Deploy on Heroku     
Please see the following [link](
https://cryptic-sea-86941.herokuapp.com/parseNbaUdn/index)

### Future work
- [ ] Index beautify
- [ ] Return data while update need to limit size in some way
- [ ] Loading more button need to disable while oldest post has been loaded

Developed by 陳冠綸 Kuan-Lun Chen