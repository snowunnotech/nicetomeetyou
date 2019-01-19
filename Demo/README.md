## py-django-demo

## QA
第一次使用django框架，對於架構還是懵懵懂懂，有不足之處也請多指教。

 1) **抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞**
> 爬蟲的程式位於src/GetNews/apps.py

 2) **使用 Django 設計恰當的 Model，并將所抓取新聞存儲至 DB。**
> 我使用內建的SQLites當資料庫<br/>將新聞獲取並存至DB的Action為<br/>https://lanmor-py-demo-lanmorop01.c9users.io/UpdateNBANews<br/>
資料庫內容可以至以下連結檢視<br/>[django admin管理](https://lanmor-py-demo-lanmorop01.c9users.io/admin)<br/>
Username:demo<br/>
Password:demodemo123

 3) **使用 Django REST Framework 配合 AJAX 實現以下頁面：**
    - **焦點新聞列表**
    - **新聞詳情頁面**
> 我將列表與詳情做在同一個頁面上<br/>新聞列表(左邊框架)用Ajax獲取Rest API內容<br/>
再以點擊各個新聞標題非同步至右邊框架<br>
[新聞列表主頁面](https://lanmor-py-demo-lanmorop01.c9users.io/NewsList)<br/>
[DRF主頁面](https://lanmor-py-demo-lanmorop01.c9users.io/api/)

 4) **以 Pull-Request 的方式將代碼提交。**
> https://github.com/bb3en/django-demo

#### **進階要求**

 1) **實現爬蟲自動定時抓取。**
> 定時抓取程式為src/RunScheduler.py<br/>
以requests.get(Update_News_URL)方式定時更新新聞至資料庫，<br/>也可以用crontab實現，只是我剛好有之前寫好的Scheduler程式。

 2) **每當抓取到新的新聞時立即通知頁面。**
> 同樣位於[新聞列表主頁面](https://lanmor-py-demo-lanmorop01.c9users.io/NewsList)，<br/>
以Javascript方式設定setInterval來更新列表，<br/>一但有最新的出現將會出現alert("有新的新聞!")，
<br/>js位於src/static/js/news.js

 3) **将本 demo 部署至服务器并可正确运行。**
> 此實作以Cloud9雲端伺服器(免費版)運行服務。
 
## 筆記

操作版本資訊
> python = 2.7.6 , django = 1.11.18

> python3.6 = 3.6.3 , django = 2.1.5

啟用服務
 > sudo python src/manage.py runserver $IP:$PORT
    
 > sudo python3.6 src/manage.py runserver $IP:$PORT
 
新增App目錄
 > python src/manage.py startapp AppName
 
新增model 
 > sudo python3.6 src/manage.py makemigrations appName

同步Model to sqlite3
 > sudo python3.6 src/manage.py migrate
    
創建AdminUser
 > sudo python src/manage.py createsuperuser
 
## 參考

Django基礎概念和MVT架構
 > https://hk.saowen.com/a/fbc2bc5a84117a1d3aa144a05c71805320cedbb746642297dd72f35ba03e8dcf

DRF從無到有
 > https://github.com/twtrubiks/django-rest-framework-tutorial

簡易配置js css
 > http://hugo-python3.blogspot.com/2014/03/django-static-file-template-inclde.html
 
