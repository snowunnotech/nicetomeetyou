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

## Answer
1. 使用docker-compose部屬 django/nginx/rabbitmq/celery container
2. 啟動API container，部屬Django REST WEB
3. 啟動Nginx container，作為Django web server
4. 啟動RMQ container，作為Celery broker
5. 啟動Celery container，每5分鐘執行爬蟲task
6. 部屬於GCP上: http://35.185.173.110 


