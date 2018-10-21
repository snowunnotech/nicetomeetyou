# nice to meet you
- [x] 1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
- [x] 2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
- [x] 3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 * 焦點新聞列表
	 * 新聞詳情頁面
- [x] 4. 以 Pull-Request 的方式將代碼提交。

## 進階要求
1. 實現爬蟲自動定時抓取。 (應該算完成一半，目前是使用client去戳server來實現爬蟲若有新的新聞將會通知client)
- [x] 2. 每當抓取到新的新聞時立即通知頁面。
3. 将本 demo 部署至服务器并可正确运行。

## 環境
1. python 3.6.6
2. django 2.1

## 安裝
```sh
pip install pipenv
pipenv --python 3.6
pipenv install
```
## 執行
```sh
pipenv run python .\manage.py runserver
```
