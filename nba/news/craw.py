import requests
from bs4 import BeautifulSoup as soup

def newscraw():
	url = 'https://nba.udn.com/nba/index?gr=www'

	data_req = requests.get(url).text
	data_soup = soup(data_req,'html.parser')
	news = data_soup.find(id="news_body")
	ret = []
	for article in news.find_all("dt"):
		title = article.find("h3").string
		content = article.find("p").string
		link = "https://nba.udn.com/"+article.find("a").get("href")
		full_req = requests.get(link).text
		full_soup = soup(full_req,'html.parser')
		storybody = full_soup.find(id="story_body_content").find("span",recursive=False).find_all("p",recursive=False)
		fulltext = ""
		for i in storybody[1:] :
			fulltext+=i.get_text().encode('utf-8')
		
		ret.append({'title':title,'content':content,'link':link,'fulltext':fulltext})
	return ret

if __name__ == "__main__":
	print newscraw()[0]['fulltext']