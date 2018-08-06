# nice to meet you


[已完成]
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。

2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。

3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
	   (以bootstrap modal+ajax 開啟內頁)
	   
4. 以 Pull-Request 的方式將代碼提交。
	
## 進階要求
1. 實現爬蟲自動定時抓取    2. 每當抓取到新的新聞時立即通知頁面。
	(撰寫custom command 供cron tab 執行, 命令包含爬資料以及將新增的資料以websocket方式傳送至client)


[未完成]
3. 将本 demo 部署至服务器并可正确运行。
    目前僅將server以<a href="http://163.13.127.195:8000/myNBAfeed">development server</a>方式運行


