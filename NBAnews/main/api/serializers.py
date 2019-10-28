from rest_framework import serializers
from main.models import imgnews

# 使用rest_framework 建立RESTful API
# 建立API的格式
# class Meta:
#      model =建立API 的 model
#      fields = API建立 的 內容物(model結構)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = imgnews
        fields = ('id', 'title', 'content', 'time', 'img')
