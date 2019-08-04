import uuid
from django.db import models


class HotNews(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    contents = models.TextField()

    #Serialization for returning as json
    @property
    def hot_news_to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    @property
    def _to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data