from rest_framework import serializers
from newsboard.models import NewsArticle



class NewsBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        # fields = '__all__'
        fields = ('title', 'content')