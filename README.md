## Done:（完成兩種環境設計: docker, virtual env）
1. 完成抓取 nba焦點新聞。
2. 使用 mysql 將所抓取新聞存儲至 DB。
3. 使用 [Django REST Framework]配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。
5. 實現爬蟲自動定時抓取。(每20秒 爬一次蟲)

![GitHub Logo](https://github.com/ekils/nicetomeetyou/blob/master/CW/img/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202018-08-19%20%E4%B8%8B%E5%8D%889.14.10.png)
![GitHub Logo](https://github.com/ekils/nicetomeetyou/blob/master/CW/img/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202018-08-19%20%E4%B8%8B%E5%8D%889.16.52.png)

</br>




## not yet:
1. 每當抓取到新的新聞時立即通知頁面。
(已完成webconnect，待抓取db的數據更新後透過websocket推播。看是要用@receiver  或直接count 做db更新通知)

2. 将本 demo 部署至服务器并可正确运行。
(之前已嘗試過在家自架伺服器。)
