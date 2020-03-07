import requests
import re
from bs4 import BeautifulSoup
import datetime
from .models import NBASpotNews
from threading import Timer
from slugify import slugify

MAX_PARSE_PAGE_COUNT = 3

CONTINUE_PARSE = 0
END_PARSE = 1

PROFILE_NOT_EXIST = 0
PROFILE_EXIST = 1


main_page = 'https://nba.udn.com/nba/cate/6754/-1/newest/'
news_content_page = 'https://nba.udn.com'

def get_news_detail(url):
	req = requests.get(news_content_page + url)
	if req.status_code == requests.codes.ok:
		all_pages = BeautifulSoup(req.text, 'html.parser')
		
		report_content = get_report_content(all_pages)
		report_time, report_source = get_report_time_and_author(all_pages)

	return report_content, report_time, report_source 

def get_report_content(all_pages):

	### Get Report content ###
	content = all_pages.find("div", {"id": 'story_body_content'}).find_all("p")
	content_without_span = []
	for s in content:
		content_without_span += [i for i in s.contents if isinstance(i, str)]
	content_without_span = "".join(content_without_span)
	return content_without_span

def get_report_time_and_author(all_pages):
	time_source = all_pages.find("div", {"class": "shareBar__info--author"})
	report_time, report_source = time_source.span.contents[0], time_source.contents[1]
	report_time = datetime.datetime.strptime(report_time, "%Y-%m-%d %H:%M")

	return report_time, report_source

def get_news(page_number, profile_exist):
	latest_news_title = ''
	last_updated_news_title = ''

	r = requests.get(main_page + str(page_number))
	if r.status_code == requests.codes.ok:
		all_pages = BeautifulSoup(r.text, 'html.parser')
		news_list_body = all_pages.find(id = "news_list_body")
		title = news_list_body.find_all("h3")
		report_url =  news_list_body.find_all("a")
		photo_url_body = news_list_body.find_all("img", class_ = "lazyload")

		# Store latest news_title to judge if there are news updated in the next period.
		if (page_number == 1 and profile_exist == PROFILE_NOT_EXIST):
			write_latest_news_file(title[0].text)
		if (page_number == 1 and profile_exist == PROFILE_EXIST):
			latest_news_title = title[0].text
			last_updated_news_title = read_latest_news_file()

		if (profile_exist == PROFILE_EXIST):
			if (last_updated_news_title == latest_news_title):
				return END_PARSE
		
		for idx, title_name in enumerate(title):
			report_content, report_time, report_source = get_news_detail(report_url[idx].get('href'))
			photo_url = photo_url_body[idx].get('data-src')
			if (profile_exist == PROFILE_EXIST):
				if (title_name.text is last_updated_news_title):
					write_latest_news_file(latest_news_title)
					return END_PARSE
			
			slug = slugify(title_name.text)
			news_detail = NBASpotNews(news_title = title_name.text, report_time = report_time, report_source = report_source, 
				report_url = news_content_page + report_url[idx].get('href'), photo_url = photo_url, content = report_content, slug = slug)
			news_detail.save()
	return CONTINUE_PARSE

def parse_multiple_pages(profile_exist):
	'''
	Only parse MAX_PARSE_PAGE_COUNT pages
	'''
	print ('Gogogo')
	for page_number in range(1, MAX_PARSE_PAGE_COUNT + 1):
		if (get_news(page_number, profile_exist) == END_PARSE):
			return

def execute_timer():
	if (check_profile_exist()):
		parse_multiple_pages(PROFILE_EXIST)
	else:
		parse_multiple_pages(PROFILE_NOT_EXIST)
	t = Timer(60, execute_timer)
	t.start()

def read_latest_news_file():
	latest_news_title = ""
	with open(LATEST_NEWS_PROFILE_PATH, 'r') as read_file:
		latest_news_title = read_file.read()
	return latest_news_title

def write_latest_news_file(latest_news_title):
	write_file = open(LATEST_NEWS_PROFILE_PATH, 'w')
	write_file.write(latest_news_title)
	write_file.close()

def check_profile_exist():
	try:
		f = open(LATEST_NEWS_PROFILE_PATH, 'r')
	except IOError:
		return PROFILE_NOT_EXIST
	f.close()
	return END_PARSE

if __name__ == "__main__":
    news = get_news()
