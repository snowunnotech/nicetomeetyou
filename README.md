# nice to meet you
(全部完成)
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。 完成
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。  完成
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表  完成
	 * 新聞詳情頁面  完成
4. 以 Pull-Request 的方式將代碼提交。  完成
	
## 進階要求
(5. 未完成)
1. 使用 Scrapy。  完成
2. 實現爬蟲自動定時抓取。  完成(使用bs4實現。)
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。  完成(但有bug，重新整理頁面後會失效，所以佈署到Heroku的版本沒有使用。)
4. 将本 demo 部署至服务器并可正确运行。  完成
5. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。


# 開發環境(windows)：
python==3.5.1  
Django==1.11.6  
djangorestframework==3.5.1  
dwebsocket==0.5.12  
Scrapy==1.6.0  
APScheduler==2.1.2  
requests==2.23.0  
beautifulsoup4==4.9.0  
Twisted==18.9.0  

# Heroku網址：
https://djangobyjamie.herokuapp.com/  
