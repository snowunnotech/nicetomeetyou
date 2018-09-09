from rest_framework import serializers
from .models import FocusNew

class FocusNewSerializers(serializers.ModelSerializer):
    class Meta:
        model = FocusNew
        fields = '__all__'
