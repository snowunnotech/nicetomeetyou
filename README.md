# nice to meet you
- [x] 1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
- [x] 2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
- [x] 3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面

- [x] 4. 以 Pull-Request 的方式將代碼提交。

## 進階要求
- [x] 1. 實現爬蟲自動定時抓取。
  - 可以使用 [django-cron](https://django-cron.readthedocs.io/en/latest/installation.html)，但我比較習慣使用 Linux 指令 `crontab -e` 定時呼叫 scripts 執行。
- [ ] 2. 每當抓取到新的新聞時立即通知頁面。
- [ ] 3. 将本 demo 部署至服务器并可正确运行。
	- 技術使用 Gunicorn, Supervisor 和 Nginx，但我來不及做完 XD

## Demo 

1. Django Framework API

![](https://i.imgur.com/NDAeY4u.png)

2. Homepage
![](https://i.imgur.com/mKE0eVf.png)

3. Story

![](https://i.imgur.com/JKR9CGv.png)