# nice to meet you
v 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。

v 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。

v 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
(前端後端分離，額外使用vue以axois呼叫Djangp api)

v 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
x 使用 Scrapy。
v 實現爬蟲自動定時抓取。
（使用apscheduler 整點0分定時爬取）

x 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。
v 将本 demo 部署至服务器并可正确运行。
（部署於AWS ec2 http://3.112.191.59）

x 所實現新聞列表 API 可承受 100 QPS 的壓力測試。

## Usage

```shell
#To Build Docker
docker-compose build

#To Run Docker
docker-compose up -d

#Migrate Database

docker ps
docker exec -t -i [container ID] bash

	#-in bash-
	
	python manage.py makemigrations
	python manage.py migrate
	
# Remove any anonymous volumes attached to containers
docker-compose down -v
```
