# How to use

* before all else, start a virtual enviornment by 
```bash
python -m venv venv
pip install -r requirements.txt
```

* first initiate scrapyd by going into dscrapy/scrapy_app and type

```bash
scrapyd
```

(however in the venv I ran into trouble I couldn't solve... see note)

* second, go to dscrapy and run the server by
```bash
python manage.py runserver
```

* there are currently four buttons at home:
	* Start Crawl: will send a POST signal to scrapyd api and start the crawling process.  Notify the frontend when finished.
	* Get REST API: will get the json from REST API and render them to HTML.
	* CleanUp DataBase: delete all records in the DataBase table.
	* Manual Refresh: as the name suggests, reload home.


# Acknowledgement: 

This project is from ChuangShun before interview.

Most of the framework are inspired by this [article] (https://medium.com/@ali_oguzhan/how-to-use-scrapy-with-django-application-c16fabd0e62e)

As well as the [Scrapyd-Django-Template] (https://github.com/adriancast/Scrapyd-Django-Template)

Most of the JS implementation are from this [repository] (https://github.com/copyNdpaste/scrapy-with-django)


### Improvements that I can think of:

  * an elegant way to automatically scrape and ajax the data to web
  * deployment? pressure test(s)?
