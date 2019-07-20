import requests
from bs4 import BeautifulSoup as bs
from nba_news.models import News

data_list = []


def crawl():
    for i in range(1, 20):
        res = requests.get("https://nba.udn.com/nba/cate/6754/-1/newest/" + str(i))
        soup = bs(res.text, 'lxml')
        news_table = soup.select("#news_list_body > dl > dt ")


        seq = ('title', 'link', 'img', 'time', 'article', 'video')
        head_url = "https://nba.udn.com"

        for item in news_table:

            # declare a dictionary for data
            data_dict = dict.fromkeys(seq)
            article = ""
            
            data_dict['title'] = item.h3.text                       # news title
            data_dict['link'] = head_url + item.a['href']           # news link
            
            # get into the article and crawl other contents
            res = requests.get(data_dict['link'])
            soup = bs(res.text, 'lxml')
            content = soup.select("#story_body_content")[0]

            data_dict['time'] = content.select("div.shareBar__info--author > span")[0].text         # news time
            

            for sentence in content.select("span > p")[1:]:                                         # news article
                article += sentence.text
            data_dict['article'] = article
            
            
            try:                                                                                    # try to find if there's a video in the news 
                video_link = content.select("div.video-container")[0].iframe['src']                 # if no, then pass
                data_dict['video'] = video_link
                data_dict['img'] = content.img['data-src']                                          # news image
            except:
                data_dict['video'] = ""
                
            if data_dict in data_list:                                                              # if there's new news, store it to data list
                return                                                                              # continue the loop until the news is duplicated
            data_list.append(data_dict)

            while len(data_list) > 200:
                data_list.pop()

        print("Crawling {} pages of news".format(i))
    save_data()


def save_data():
    count = 0
    data_list.reverse()
    for item in data_list:
        count += 1
        News.objects.get_or_create(title=item['title'],
                                    link=item['link'],
                                    img=item['img'],
                                    time=item['time'],
                                    article=item['article'],
                                    video=item['video'])
        
        print('Crawling and deposit {} data'.format(count))

crawl()