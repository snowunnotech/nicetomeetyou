from rest_framework import serializers
from warehouse.models import TopNews


class TopNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopNews
#        fields = ('id', 'link', 'photo', 'headline', 'body')
        fields = '__all__'
