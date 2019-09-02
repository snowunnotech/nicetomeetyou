from rest_framework import serializers
from .models import NBAHotNews


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBAHotNews
        # fields = '__all__'
        fields = ['NewsId', 'NewsTitle', 'NewsUpdateDateTime', 'Author', 'ImgFileName']

class NewsDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = NBAHotNews
		fields = ['NewsTitle', 'Author', 'NewsUpdateDateTime', 'NewsDetailContent']

