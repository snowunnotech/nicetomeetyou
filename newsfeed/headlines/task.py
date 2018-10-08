from bs4 import BeautifulSoup
from datetime import datetime
from .models import HeadlinePost
import requests
import re
import urllib.parse as urlp

url_base = 'https://nba.udn.com/'
url_newsfeed = 'nba/cate/6754'

def getSoup(url, parser='html.parser'):
	r = requests.get(url)
	content = r.text
	soup = BeautifulSoup(content, 'html.parser')
	return soup

def getNewsFeed():
	post_list = []

	# info in newsfeed
	soup_post_list = getSoup(urlp.urljoin(url_base, url_newsfeed))
	for p in soup_post_list.select('#news_list_body dl dt a'):
		
		post_id = int(p.get('href')[-7:])

		if HeadlinePost.objects.filter(post_id=post_id).exists():
			continue

		post_title = p.select('h3')[0].get_text()
		post_url = urlp.urljoin(url_base, p.get('href'))
		img_url = p.select('span img')[0].get('data-src')

		# info in newsfeed/post
		soup_post = getSoup(post_url)
		post_date = soup_post.select('.shareBar__info--author span')[0].get_text()
		post_date = datetime.strptime(post_date, '%Y-%m-%d %H:%M')
		
		post_content = ""
		for c in soup_post.select('#story_body_content span p'):
			post_content += str(c)

		# add new post to list
		post_list.append({'post_id': post_id, 
			'post_title': post_title,
			'post_url': post_url, 
			'img_url': img_url,
			'post_date': post_date, 
			'post_content': post_content})


	# save to db
	print('#post_list is saved : {}'.format(len(post_list)))
	for post in post_list:
		new_post = HeadlinePost(post_id=post['post_id'], 
				post_title=post['post_title'],
				post_url=post['post_url'], 
				img_url=post['img_url'],
				post_date=post['post_date'], 
				post_content=post['post_content'])
		new_post.save()
