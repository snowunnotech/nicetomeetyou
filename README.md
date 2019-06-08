# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
4. 以 Pull-Request 的方式將代碼提交。

## 進階要求
1. 實現爬蟲自動定時抓取。
2. 每當抓取到新的新聞時立即通知頁面。
3. 将本 demo 部署至服务器并可正确运行。

## Document
- 使用 pipenv 作 virtualenv
- 採 gitflow 開發
- ajax code: test.js and test_detail.js
- 焦點新聞列表：http://127.0.0.1:8000/news/index/
- test
  - python3 -m unittest crawler.tests.test_parser
  - python3 -m unittest crawler.tests.test_scraper
  - python3 manage.py test news.helpers.tests.test_scrapy --keepdb -v2
