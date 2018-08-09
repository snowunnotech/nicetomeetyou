from rest_framework import serializers
from chat.models import Post,Paragraph




class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(many=True,read_only=True)

    class Meta:
        model = Post
        fields = ('id','title', 'orig_date', 'reporter','paragraphs')