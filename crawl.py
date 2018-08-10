from bs4 import BeautifulSoup
from datetime import datetime
import requests
import psycopg2

HOST = 'https://nba.udn.com'
URL = HOST + '/nba/index?gr=www'


def get_web_page(url):
    '''
    Try to get the target page with requests.
    '''
    try:
        resp = requests.get(url=url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            return soup
        else:
            print('Wrong status code:', resp.status_code)
            return None
    except TypeError:
        print('Cannot get web page')
        return None


def connect_db():
    '''
    Get the connection to the postgreSQL.
    '''
    conn = psycopg2.connect(
        database="dg62hgin80pv3",
        user="mblkytpskwbsjl",
        password="8959ea54deffcbda363077049518915120a33eb2efb5677091a379a1604b6068",
        host="ec2-54-225-76-201.compute-1.amazonaws.com",
        port="5432"
    )
    return conn


def is_new(conn, dt):
    '''
    Check if the news has already existed in the database.
    '''
    # get urls of news
    href = dt.a['href']
    url = HOST + href

    # check if the news exists
    cur = conn.cursor()
    cur.execute('SELECT url FROM main_news;')
    old_newses = cur.fetchall()
    if url in [old_news[0] for old_news in old_newses]:
        return False
    return url


def crawl_and_save(conn, url):
    '''
    Crawl the detail page of news, clean the data and save to DB.
    '''
    soup = get_web_page(url)
    title = soup.find("h1", "story_art_title").text
    pub_time = soup.find("div", "shareBar__info--author").span.text
    pub_time = datetime.strptime(pub_time, '%Y-%m-%d %H:%M')
    crawl_time = datetime.now()
    paragraphs = soup.find("div", id="story_body_content").find_all("span")[2].find_all("p")

    # clean the content data
    content = ''
    for paragraph in paragraphs:
        if paragraph.find("figure"):
            continue
        content += paragraph.text

    # save to database
    cur = conn.cursor()
    cur.execute('''INSERT INTO main_news (
        title,
        url,
        pub_time,
        crawl_time,
        content) VALUES (%s, %s, %s, %s, %s)''', (
        title,
        url,
        pub_time,
        crawl_time,
        content,
    ))
    conn.commit()


def main():
    '''
    Find the target urls, and run the crawling process.
    '''
    conn = connect_db()
    soup = get_web_page(URL)
    dts = soup.find("div", id="news").find_all("dt")
    for dt in dts:
        url = is_new(conn, dt)
        if url:
            crawl_and_save(conn=conn, url=url)
    conn.close()


if __name__ == '__main__':
    main()
