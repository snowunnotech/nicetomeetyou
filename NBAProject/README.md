# NBAProject

### NBA 新聞網頁爬蟲並實作網頁呈現  
### 使用環境與工具 Windows10, python3.7.3, Scrapy, Django, Django REST Framework, AJAX
#### 未完成：
* 使用 Websocket 服務，抓取到新的新聞時立即通知前端頁面
* 将本 demo 部署至服务器并可正确运行
* 所實現新聞列表 API 可承受 100 QPS 的壓力測試

### 安裝步驟
1. clone or download the project  
`git clone https://github.com/nunuku951753/nicetomeetyou.git `

2. 建置image  
`$ docker build -t nba-web . ` 

3. 啟用並進入container  
`$ docker run -p 8000:8000 -it [image id] /bin/bash `

4. 啟動server  
`python manage.py runserver 0.0.0.0:8000 `

5. 網址：http://192.168.99.100:8000/base/ (使用docker ip)

### Scrapy啟動步驟
1. 進入執行中的container  
`$ docker exec -it [container id] /bin/bash `  

2. 於container內執行程式  
至爬蟲目錄: `cd nba_bot `  
    * 單次爬蟲：
    `scrapy crawl nba `  
      
    * 定時爬蟲：
    `python main.py --job nba --freq 10`
        * job - scrapy job name  
        * freq - 頻率(單位/秒)
