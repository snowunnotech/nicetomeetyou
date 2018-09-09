from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.request import urlopen
import requests
import re
import datetime
import sqlite3

def find_focus_new():
    html = urlopen("https://nba.udn.com/nba/index?gr=www").read().decode("utf-8")
    soup = BeautifulSoup(html,'html.parser')
    for h1 in soup.find_all('h1', class_= "box-title"):
        if h1.a == None:
            break
        try:
            link = re.search('(?<=href=")[a-z0-9/]+', str(h1.a))
            return link.group(0)
        except:
            break

def get_all_news():
    link = "https://nba.udn.com" + str(find_focus_new)
    #print(link)
    html = urlopen(link).read().decode("utf-8")
    soup = BeautifulSoup(html,'html.parser')
    for a in soup.find_all('a', class_= "active"):
        print(a)

def get_focus_new():
    html = urlopen("https://nba.udn.com/nba/index?gr=www").read().decode("utf-8")
    soup = BeautifulSoup(html,'html.parser')
    linklist = []
    for dt in soup.find_all('dt'):
        if dt.a == None:
            break
        try:
            link = re.search('(?<=href=")[a-z0-9/]+', str(dt.a))
            complete_link = "https://nba.udn.com" + str(link.group(0))
            linklist.append(complete_link)
        except:
            continue

    return linklist

def get_content(link):
    #print(link)
    focus_new = []
    focus_new.append(link)
    html = urlopen(link).read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    title = get_content_title(soup)
    focus_new.append(title)
    time_info = get_post_time(soup)
    focus_new = focus_new + time_info
    content = []
    for p in soup.find_all('p'):
        img_src = re.search('(?<=data-src=")[^;]+',str(p))
        if img_src:
            focus_new.append(img_src.group(0))
            #print(img_src.group(0))
        else:
            content.append(str(p))
    focus_new.append(sentence_filter(content))
    #print(focus_new)
    return focus_new

def get_content_title(soup):
    for h1 in soup.find_all('h1', class_="story_art_title"):
        story_title = re.search('(?<=story_art_title">)[^<]+', str(h1))
    return story_title.group(0)

def sentence_filter(content):
    story = ''
    for sentence in content:
        if re.search(r'video-container', sentence):
            continue

        if re.search(r'blockquote', sentence):
            continue

        if re.search(r'twitter', sentence):
            continue
       
        sentence = BeautifulSoup(sentence, 'html.parser')
        if sentence.get_text() != '':
            story = story + sentence.get_text() + '\n'
        #print(story)
    return story

def get_post_time(soup):
    for div in soup.find_all("div", class_ = "shareBar__info--author"):
        time_info = BeautifulSoup(str(div), 'html.parser')
        time_info = time_info.get_text(',').split(',')
        #time_info[0] = time_info[0].strftime('%Y-%m-%dT%H:%M:%S')
    return time_info

def insert_data(data):
    conn = sqlite3.connect('/home/lieric7766/nba/db.sqlite3')
    #print(conn)
    cursor = conn.cursor()
    check_string = "SELECT * FROM focusNew_focusnew WHERE title='"+ data[1] + "'"
    #print(check_string)
    for a in cursor.execute(check_string):
        if a[1] == data[1]:
            return 0
    insert_string = "INSERT INTO focusNew_focusnew (title, post_time, writer, img_src, content) Values(" + '"' + data[1] + '","' + data[2] +'","' + data[3] + '","' + data[4] + '","' + data[5] + '")' 
    cursor.execute(insert_string)
    conn.commit()
    conn.close()

def drive():
    link_list = get_focus_new()
    for link in link_list:
        #print(get_content(link))
        data = get_content(link)
        check = insert_data(data)
        if check == 0:
            print("already exist!!")

drive()

