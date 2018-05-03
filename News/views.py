from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from News.models import Article
from channels import Group
from channels.sessions import channel_session

# Serializers define the API representation.
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'url', 'img_url', 'content', 'time')

# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

def getLastRecords():
    if Article.objects.order_by('-time').exists():
        lastArticle = Article.objects.all().orderby('-time')[0]
        return lastArticle



@channel_session
def ws_connect(message):
    Group('News').add(message.reply_channel)
    message.channel_session['News'] = "news"
    # Accept the connection request
    message.reply_channel.send({"accept": True})

@channel_session
def ws_receive(message):
    m = getLastRecords()
    Group('News').send({'data': json.dumps(m)})

@channel_session
def ws_disconnect(message):
     print ("disconnect", message)

