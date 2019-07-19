# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。(O)
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。(O)
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：(O)
	 * 焦點新聞列表
	 * 新聞詳情頁面
(前端後端分離，額外使用vue以axois呼叫Djangp api)
4. 以 Pull-Request 的方式將代碼提交。(O)

## 進階要求
1. 使用 Scrapy。(X)
2. 實現爬蟲自動定時抓取。(O)
(使用apscheduler 整點0分定時爬取）
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。(X)
4. 将本 demo 部署至服务器并可正确运行。(O)
（部署於AWS ec2 前端demo page:http://3.112.191.59）
5. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。(X)
	
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
