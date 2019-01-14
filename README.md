# 使用說明
在專案根目錄下使用 docker-compose 啟動各項服務
```
docker-compose up --build
```
待啟動完畢後，訪問新聞列表，一分鐘後爬蟲完成爬取資料後會通知更新頁面。  
[http://localhost](http://localhost)  
  
造訪管理員頁面，帳:admin 密:secret  
[http://localhost/admin](http://localhost/admin)

# 實作進度說明
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。  
完成，頁面中的三篇焦點新聞皆可正確抓取，並有處理掉內文中的 html tags  
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。  
完成，新聞皆存儲至DB  
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面  
完成，以 Vue.js 搭配 FetchAPI 實作  
4. 以 Pull-Request 的方式將代碼提交。  
完成
	
## 進階要求
1. 實現爬蟲自動定時抓取。
完成，每分鐘會自動檢查有無新新聞。  
2. 每當抓取到新的新聞時立即通知頁面。  
完成，當有發現新新聞會在10秒內通知使用者刷新頁面。本功能可使用admin頁面手動新增文章測試。    
3. 将本 demo 部署至服务器并可正确运行。  
完成，部署於nginx上，前後端分離，並以nginx提供靜態內容。

