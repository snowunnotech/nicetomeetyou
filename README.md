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

## 執行  
`python manage.py qcluster`  
`python manage.py runserver 0.0.0.0:8000`    

## 完成  

1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。  
檔案放在`nicetomeetyou/NBA_Crawler_Web/nba_crawler_web/news/nba_crawler.py`  
以requests、BeautifulSoup、lxml實現抓取網頁資訊，並利用Django的Model存進資料庫中。  

2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。  
資料庫規劃如下:  
將datetime和title設為unique together，防止儲存重複的新聞。  

|       Name        |  author  |  datetime  |  title  |  image_url  |  story_url  |  content  |  video_url  |
|:-----------------:|:--------:|:----------:|:-------:|:-----------:|:-----------:|:---------:|:-----------:|
|  unique together  |          |     *      |    *    |             |             |           |             |
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：  
	 * 焦點新聞列表  
	 * 新聞詳情頁面  


4. 實現爬蟲自動定時抓取。  
使用django-q來處理排程。  
登入admin頁面後，點選Django Q -> Schedule tasks -> Add到新增的頁面上做設定。  
Ex: 每分鐘執行一次爬蟲。  
```
Name: crawler
Func: news.tasks.crawler

Schedule Type: Minutes
Minutes: 1
Repeats: -1
```  
並執行`python manage.py qcluster`  

## 未完成  
1. 每當抓取到新的新聞時立即通知頁面。  
2. 将本 demo 部署至服务器并可正确运行。  
