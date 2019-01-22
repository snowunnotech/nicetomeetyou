# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。  
   已成功爬取 新聞標題、圖片、內文、連結、時間
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。  
    爬取資料後判斷是否存在後會自動存入資料庫  
    以下為 Model  
    news_title = 新聞標題      
    news_link = 連結      
    news_content = 內文      
    news_img = 圖片  
    news_time = 時間  
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：  
     使用DRF序列化資料，並使用ajax撈取  
     使用ajax在焦點新聞列表頁面異步更新新聞詳細內容  
4. 以 Pull-Request 的方式將代碼提交。
    
## 進階要求
1. 實現爬蟲自動定時抓取。  
   使用apscheduler每10分鐘進行一次爬蟲，並在pythonwhere的Bash執行  
2. 每當抓取到新的新聞時立即通知頁面。  
   未完成  
3. 将本 demo 部署至服务器并可正确运行。  
   部署到 pythonanywhere
   http://nbanews.pythonanywhere.com
