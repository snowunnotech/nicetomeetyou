
from news.models import newscatch 
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class newscatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = newscatch
        fields = ('ID','title','time','cotent','img')            