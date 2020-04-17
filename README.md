# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
1. 使用 Scrapy。
2. 實現爬蟲自動定時抓取。
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。
4. 将本 demo 部署至服务器并可正确运行。
5. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。


# 答題
1. 使用 Scrapy 抓取焦點新聞，由於觀察新聞更新速度大約一小時一次，因此爬的頻率也是設成一小時
	- settings.py: `CRONJOBS = [('0 * * * *', 'run_crawler.start_crawler')]`
	- 由於需要給 crontab 執行，因此把執行爬蟲改成需要跑 run_crawler.py
2. 透過 scrapy-djangoitem 在每次 Scrapy 爬完新聞時，儲存至 Django 內建的 sqllite3
3. 由於 Restful API 有固定的風格，且前端只會使用 GET 獲取新聞，因此這裡沒有使用 Django REST Framework

## 進階要求
1. 有使用 Scrapy
2. 使用 django-crontab 達成，或直接在 linux 下用 crontab 也可以，這裡沒用 sleep 或其他寫死的方式，是因為覺得這樣很怪
3. 後端使用 channels，前端使用 Websocket 物件，前端可以在 console 裡看到更新紀錄
4. [部署到這裡](http://f1238762001.pythonanywhere.com/)
	- 由於 channels 有使用到 asgi，免費的部署平台似乎都不支援它，因此沒有 Websocket 的功能
	- 且因為是免費帳戶，PythonAnywhere 只允許透過 proxy 去連它白名單的網站，所以沒辦法跑爬蟲...
	- 目前網頁能顯示東西是因為我把我的 local db 上傳上去，另外重複的內容是我測試時留下的，pr 裡的已經不允許重複寫入
5. 不太清楚要怎麼做測試
