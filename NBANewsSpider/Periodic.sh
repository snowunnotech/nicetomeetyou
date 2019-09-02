#!/bin/bash
echo "Running Spider"
export PATH=/home/psyman/.local/bin:$PATH
cd /home/psyman/WorkSpace/nicetomeetyou/NBANewsSpider/
scrapy crawl NBANewsSpider
