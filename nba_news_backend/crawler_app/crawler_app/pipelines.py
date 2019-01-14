# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from backend_app.serializers import ArticleItemSerializer, TaskItemSerializer
from backend_app.models import TaskItem

class CrawlerAppPipeline(object):
    """
    Pipeline for crawler_app
    """
    def __init__(self, jobid):
        """
        constructor: get attrs and save
        """
        self.jobid = jobid

    @classmethod
    def from_crawler(cls, crawler):
        """
        get job_id, max_retry, max_articles from crawler (given by scrapyd)
        """
        return cls(jobid=getattr(crawler.spider, '_job'))

    def open_spider(self, spider):
        """
        when an spider opens, register its task in the db
        """
        task = {'jobid': self.jobid}
        serializer = TaskItemSerializer(data=task)
        # if data is valid
        if serializer.is_valid():
            # save data into db
            serializer.save()
        else:
            print('data is not valid: '+str(serializer.errors))


    def process_item(self, item, spider):
        """
        save article to db
        """
        article = {
            'publish_dt': item['publish_dt'],
            'title': item['title'],
            'url': item['url'],
            'author_info': item['author_info'],
            'content': item['content'],
            't_id': self.jobid
        }
        
        serializer = ArticleItemSerializer(data=article)
        # if data is valid
        if serializer.is_valid():
            # save data into db
            print('[ArticleItem] we found a new article')
            serializer.save()
        else:
            print('[ArticleItem] data is not valid: '+str(serializer.errors))

        return item

    def close_spider(self, spider):
        """
        when an spider closes, update its task status in the db
        """
        try:
            task = TaskItem.objects.get(pk=self.jobid)
        except TaskItem.DoesNotExist:
            return print('task does not exist')

        data = {
            'state': 'finished',
            'ended_dt': datetime.now()
        }
        serializer = TaskItemSerializer(task, data=data, partial=True)
        # if data is valid
        if serializer.is_valid():
            # save data into db
            serializer.save()
        else:
            print('[TaskItem] data is not valid: '+str(serializer.errors))
