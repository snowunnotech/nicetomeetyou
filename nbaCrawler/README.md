# nice to meet you
1. 抓取 https://nba.udn.com/nba/index?gr=www 中的焦點新聞。
    - done
2. 使用 [Django](https://www.djangoproject.com/) 設計恰當的 Model，并將所抓取新聞存儲至 DB。
    - done
3. 使用 [Django REST Framework](http://www.django-rest-framework.org/) 配合 AJAX 實現以下頁面：
	 - done
	 * 焦點新聞列表
	    - done
	 * 新聞詳情頁面
	    - done
4. 以 Pull-Request 的方式將代碼提交。
    - done

## 進階要求
1. 實現爬蟲自動定時抓取。
    - done
2. 每當抓取到新的新聞時立即通知頁面。
    - done
3. 将本 demo 部署至服务器并可正确运行。
    - no platform for deploy

## 運行
1. environment : Ubuntu16.04, python 3.6.4, docker, docker-compose
2. docker-compose up