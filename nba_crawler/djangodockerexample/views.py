from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render
from django.http import JsonResponse
import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", host="db", port="5432")
cur = conn.cursor()

try:
	cur.execute('''DROP TABLE nba;''')
	conn.commit()
except:
	pass
conn = psycopg2.connect(database="postgres", user="postgres", host="db", port="5432")
cur = conn.cursor()
cur.execute('''CREATE TABLE nba(index TEXT PRIMARY KEY NOT NULL,title TEXT,link TEXT);''')
conn.commit()
from bs4 import BeautifulSoup
import urllib
import urllib.request
import re

url = 'https://nba.udn.com/nba/index?gr=www'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,'lxml')
import requests
#print(soup.prettify())
p_tags = soup.find_all('p')
h3_tags = soup.find_all('h3')
a_tags = soup.find_all('a')
c=[]
d=[]
for tag in p_tags:
	#print(tag.string)
	c.append(tag.string)
#print(c)
for tag in h3_tags:
	#print(tag.string)
	d.append(tag.string)
#print(d[-6:-3])
#print(a_tags[100])
a_tag = soup.find_all(href=re.compile("^/nba/story/6780.*"))
link = []
url_new = []
for tag in a_tag:
	link.append(tag.get('href'))
for link1 in link:
	url_new.append('https://nba.udn.com' + '%s'%link1)

def title(a):
	url_new = a
	page = urllib.request.urlopen(url_new)
	soup = BeautifulSoup(page,'lxml')
	return soup.title.string[:-17]
'''
def content(a):
	url_new = a
	page = urllib.request.urlopen(url_new)
	soup = BeautifulSoup(page,'lxml')
	return soup
'''
for j in range(len(url_new)):
	title_new = title(url_new[j])
	cur.execute("INSERT INTO nba (index,title,link) VALUES (%d, '%s', '%s')"%(j,url_new[j],title_new))
	conn.commit()
'''
	#try:
	cur.execute("SELECT MAX(index) FROM nba;")##HGCN_id
	i = cur.fetchone()
	cur.execute("INSERT INTO nba (index,title,link) VALUES (%d, '%s', '%s')"%(int(i[0])+1+j,url_new[j],title_new))		
	conn.commit()
'''
	#except:
	

#for tag in a_tags:
	#print(tag.get('href'))
	#print(tag.get('href'))

#cur.execute("INSERT INTO nba (index,title,link) VALUES (%d, '%s', '%s')"%(i,url_new[i],title_new))
##HGCN_id
cur.execute("SELECT * FROM nba")
rows = cur.fetchall()
title = []
link = []
for i in range(len(rows)):
	title.append(rows[i][1])
	link.append(rows[i][2])
conn.close()
def blog_list(request):
	
	#title_new = title(url_new[i])
	context = {
	'title':title,
	'link':link}
	return JsonResponse(context)

'''
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
'''

