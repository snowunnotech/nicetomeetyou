from rest_framework import serializers
from .models import NBAnews

class newsSerializer(serializers.ModelSerializer):
  class Meta:
    model = NBAnews
    fields = '__all__'