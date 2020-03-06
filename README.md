網站目前部署在 heroku 上，網址為：https://nbaspotnews.herokuapp.com/catalog/
(目前發現有 bug，會導致產生大量的新聞資訊，此行為會導致內容頁無法進入，正嘗試修復中)

非常感謝貴公司邀請我進行這次的測驗，也希望有進一步面試的機會。
雖然之前有接觸過 Python，但對於 Django 及 rest framework 都是第一次接觸，由於時間不夠，可能做得還不夠完善或是錯誤，請見諒
若有任何意見及建議，也歡迎告知我，謝謝！

我的 email: patrick55529617@gmail.com

By Patrick Hu


# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。
	
## 進階要求(1.3.5未完成)
1. 使用 Scrapy。
2. 實現爬蟲自動定時抓取。(每 1 分鐘進行一次抓取，目前設定為抓取3頁，不過變數可調整)
3. 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面。
4. 将本 demo 部署至服务器并可正确运行。(部署在 heroku 上)
5. 所實現新聞列表 API 可承受 100 QPS 的壓力測試。
