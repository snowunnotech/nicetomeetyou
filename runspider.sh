#i/bin/bash



cd NBA/scraper 

while :
do
	scrapy runspider spiders/news_spider.py
	sleep 5
done
