import requests
from news.models import News
from bs4 import BeautifulSoup
from django.core.exceptions import ObjectDoesNotExist
import paho.mqtt.client as paho

broker = 'broker.mqttdashboard.com'
port = 8000
def on_connect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))

def on_publish(client,userdata,result):
    print("data published \n")
    pass

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def checkNewsInDb(id):
    try:
        a = News.objects.get(uuid=id)
        return True
    except ObjectDoesNotExist:
        return False

def crawlCornJob():
    client1 = paho.Client(transport="websockets")
    client1.on_publish = on_publish
    client1.connect(broker,port)

    r = requests.get('https://nba.udn.com/nba/index?gr=www')

    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text,'html.parser')
        url = []
        document = {}
        news = soup.select('#news_body > dl > dt > a')
        for s in news:
            url.append('https://nba.udn.com' + s.get('href'))

        for story in url:
            id = story.split('/')[6]
            content = requests.get(story)
            if content.status_code == requests.codes.ok:
                soup1 = BeautifulSoup(content.text, 'html.parser')
                title = soup1.select('#story_body_content > h1')[0].text
                date = soup1.select('#shareBar > div.shareBar__info > div > span')[0].text
                text_list = soup1.select('#story_body_content > span > p')
                text = ''
                for i in range(len(text_list)):
                    if i == 0:
                        pass
                    elif text_list[i].text:
                        text += text_list[i].text
                if not checkNewsInDb(id):
                    n = News.objects.create(uuid=id, title=title, published_date=date, text=text)
                    n.save()
                    ret = client1.publish('crawl',"update")










            
            

