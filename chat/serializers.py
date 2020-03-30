from rest_framework import serializers
from .models import Udn
class UdnSerializer(serializers.ModelSerializer): #對model做序列化
    class Meta:
        model = Udn
        fields = '__all__'
        # fields =["title","link","report","content"]
