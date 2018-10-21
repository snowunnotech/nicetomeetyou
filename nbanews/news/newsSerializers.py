'''
Created on Aug 23, 2018

@author: Alex
'''

from rest_framework import serializers
from news.models import News



class newsSerializer( serializers.HyperlinkedModelSerializer):

    '''
        table : news
    '''

    class Meta:

        model = News
        fields = ( 'id',
                   'time',
                   'title',
                   'content',
                   'imgsrc',
                   'detailsrc',
                 )
        #fields = '__all__'
        




