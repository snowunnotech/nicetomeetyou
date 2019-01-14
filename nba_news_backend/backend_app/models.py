"""
./backend_app/models.py
define models
"""
from django.db import models

# Create your models here.
class TaskItem(models.Model):
    """
    Crawling task
    """
    jobid = models.CharField(max_length=32, primary_key=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    ended_dt = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=12, default='initialized')
    def __str__(self):
        return '[%s] %s'%(self.state, self.jobid)
    # Meta settings for db
    class Meta:
        db_table = "crawlTasks"

class ArticleItem(models.Model):
    """
    Article content
    """
    publish_dt = models.DateTimeField()
    title = models.CharField(max_length=32)
    url = models.URLField(max_length=70, unique=True)
    content = models.TextField()
    author_info = models.CharField(max_length=32)
    t_id = models.ForeignKey(
        'TaskItem',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '[%s] %s'%(self.publish_dt, self.title)

    # Meta settings for db
    class Meta:
        db_table = "articles"
