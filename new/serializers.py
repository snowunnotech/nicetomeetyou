from django.contrib.auth.models import User
from rest_framework import serializers

from new.models import new


class NewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = new
        fields=('article','title','detail')
