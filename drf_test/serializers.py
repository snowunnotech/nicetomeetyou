from rest_framework import serializers
from drf_test.models import Nba


class NbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nba
        fields = '__all__'
        # fields = ('id', 'title', 'rel_date', 'nba_content')
