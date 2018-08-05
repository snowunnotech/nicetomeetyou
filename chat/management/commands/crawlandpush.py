from django.core.management.base import BaseCommand, CommandError
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from time import sleep
from bs4 import BeautifulSoup
import requests as r
from chat.models import Post, Paragraph


class Command(BaseCommand):
    '''to display notification sequentially, I wont use batch process'''
    def handle(self, *args, **options): 
        baseurl="https://nba.udn.com"
        response = r.get("https://nba.udn.com/nba/news/")
        soup = BeautifulSoup(response.text, "lxml") 
        
        soup=soup.select("#news_list_body dt")
        for i in soup:

            imgurl=i.select('img')[0].get('data-src')
            title=i.select('h3')[0].text
            alt=i.select('p')[0].text

            if(Post.objects.filter(title=title).count() >0 ):
                continue

            innerpage=r.get(baseurl+i.select('a')[0].get("href"))
            innerpage=BeautifulSoup(innerpage.text, "lxml") 
            pubtime=innerpage.select("#story_body_content span")[0].text
            author=innerpage.select("#story_body_content .shareBar__info--author")[0].text.replace(pubtime,"")
            newpost=Post.objects.create(title=title,orig_date=pubtime,reporter=author)
            newpost.save()
            Paragraph.objects.create(post=newpost,typ="alt",hbody=alt).save()
            Paragraph.objects.create(post=newpost,typ="thumb_url",hbody=imgurl).save()
            for i in innerpage.select("#story_body_content p"):
                    if(i.text.strip() and i.text.strip() !="NBAfacebooktwitterpinterest"):
                        Paragraph.objects.create(post=newpost,typ="p",hbody=i.text).save()
            for i in innerpage.select("#story_body_content img"):
                    Paragraph.objects.create(post=newpost,typ="inner_imgurl",hbody=i.get("data-src")).save()
            # channel_layer=get_channel_layer()
            # async_to_sync(channel_layer.group_send)("mysubscribe", { 'type': 'send_message','message': story})
            

            break
        # while True:

           
            
        #     async_to_sync(channel_layer.group_send)("mysubscribe", { 'type': 'send_message','message': "haha cmd"})
        #     sleep(5)
        #     if(count==5):
        #         return
        #     count+=1
        # self.stdout.write("Unterminated line", ending='')
        

        