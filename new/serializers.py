from django.contrib.auth.models import User
from rest_framework import serializers

from new.models import New


class NewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = New
        fields=('article','title','detail')
