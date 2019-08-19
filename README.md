# Intro
Hi I'm Adam, here's how this demo works and how to deploy it.
You can find deployed demo here on AWS:
http://ec2-3-16-219-207.us-east-2.compute.amazonaws.com:8011/webpage/nba_news_in_focus/

Not necessary but you can inspect the database via this phpmyadmin:
http://ec2-3-16-219-207.us-east-2.compute.amazonaws.com:8080/
username:user
password:123

Notice: crawler.env or .env file should add to .gitignore in real use for security purpose, they're uploaded only for demo.

# Improvement may do
1. Use redis to cache datas, make list return fast.
2. Make sure that queryset in django is a generator_like object or just a list_like object? How's the performance of looping over a queryset? Any better way to do so? 
---> Yes, queryset is list_like, but they provie a method Queryset.iterator(). For a QuerySet which returns a large number of objects that you only need to access once, this can result in better performance and a significant reduction in memory.

# Infrastructure
- Deploy on AWS EC2 free-tier
- Use docker-compose to wrap up all the following tools.
- Use Django + Nginx + uwsgi to build services, use jquery. ajax to async news list.
- Use Celery + RabbitMQ to do scheduled work, crawling down NBA news per 3 minutes.
- Use Scrapy to crawl.
- Use mysql as db.
- Apply phpmyadmin to inspect db
- Use supervisor to monitor docker-compose services, auto-restart if services down. 

# How to deploy
 - clone project
 - add mysite.sock and mkdir log into /app 
 - docker-compose up, wait for building
 - docker ps | grep api , find the container's id
 - docker exec -it <container_id> bash
 - cd app & python manage.py migrate
 - kill docker-compose process and restart, done.


# nice to meet you
(Check) 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。\
(Check) 使用 [Django](https://www.djangoproject.com/) 設計恰當的model并將所抓取新聞存儲至 DB。\
(Check) 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：\
	 (Check)* 焦點新聞列表\
	 (Check)* 新聞詳情頁面\
(Check) 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
(Check) 使用 Scrapy。\
(Check) 實現爬蟲自動定時抓取。\
(TODO) 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。\
(Check) 将本 demo 部署至服务器并可正确运行。\
(TODO) 所實現新聞列表 API 可承受 100 QPS 的壓力測試。
