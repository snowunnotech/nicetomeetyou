### 基本要求 ( 完成 )

1. 抓取 [https://nba.udn.com/nba/index?gr=www](https://nba.udn.com/nba/index?gr=www) 中的焦點新聞。
   - 使用 Scrapy 來抓取焦點新聞
<br><br>
2. 使用 Django 設計恰當的 Model，并將所抓取新聞存儲至 DB。
   - 使用 Django ORM 搭配原生的資料庫 sqlite3
   - 更改 Scrapy 設定來達到能導入 Django Models ，在 Pipeline 將 Scrapy Items 存入資料庫
   - Models 設計
      * title : 新聞標題
      * slug : unique ，使用 publish_date 當作依據  ex. http:localhost:800/detail/{slug}/{id}/
      * publish_date : 新聞發布時間
      * author : 作者
      * image_url : 圖片連結
      * image_caption : 圖片說明
      * video_url : 影片連結
      * content : 網頁中文字敘述部分
      * created : 項目創建的時間
      * read : 沒用到
<br><br>
3. 使用 Django REST Framework 配合 AJAX 實現以下頁面，焦點新聞列表 (list.html) ，新聞詳情頁面 (detail.html)
   - 通過 DRF 將 Django Models 序列化，實現 JSON 格式的 API
   - 使用 Bootstrap4 來加速網頁排版
   - 使用 jQuery 通過 AJAX 獲取 API ，並填入資訊
<br><br>

### 進階要求 ( 未完成 )

1. 實現爬蟲自動定時抓取。
   - 將 Scrapy 修改成 Django App 形式，通過 Celery 來實現定時抓取任務。
      * 目前通過網頁來讓爬蟲在 Celery 中執行，不過只能跑一次後結束會發生 Exception
<br><br>
2. 每當抓取到新的新聞時立即通知頁面
   - 通過 Django Channels 與 WebSocket 來實現當 Models 改變時實時通知頁面
      * 還沒做到這個部分
<br><br>
3. 将本 demo 部署至服务器并可正确运行
   - 部署到 Heroku
      * 要將資料部署到 Heroku 時，因為認不出程式碼語言失敗了。
