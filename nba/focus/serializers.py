from .models import Entry
from rest_framework import serializers
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id','title','author','body','created_time','modified_time')
