# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。</br>
   /news_crawler/news_crawler.py</br>

2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。</br>
   /news_crawler/crawler/models.py</br>

3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：</br>
   http://server-ip:port/api/News/</br>
	 * 焦點新聞列表</br>
	 /news_crawler/crawler/templates/index.html</br>
	 * 新聞詳情頁面</br>
	 /news_crawler/crawler/templates/news_detail.html</br>
4. 以 Pull-Request 的方式將代碼提交。</br>
	
## 進階要求
1. 實現爬蟲自動定時抓取。</br>
   Crontab設定十分鐘執行一次news_crawler.py</br>

2. 每當抓取到新的新聞時立即通知頁面。</br>
   setTimer()讀取api</br>

3. 将本 demo 部署至服务器并可正确运行。</br>
   部屬至GCE</br>
   http://35.221.159.121/
