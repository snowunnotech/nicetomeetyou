from django.utils.timezone import now
from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        # fields = ('id', 'title', 'url', 'date', 'source', 'content')

    def get_days_since_created(self, obj):
        return (now() - obj.created).days