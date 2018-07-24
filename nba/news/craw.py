import requests
from bs4 import BeautifulSoup as soup

def newscraw():
	url = 'https://nba.udn.com/nba/index?gr=www'

	data_res = requests.get(url).text
	data = soup(data_res,'html.parser')
	news = data.find(id="news_body")
	ret = []
	for article in news.find_all("dt"):
		title = article.find("h3").string
		content = article.find("p").string
		link = "https://nba.udn.com/nba/story/6780/3267970"+article.find("a").get("href")
		ret.append({'title':title,'content':content,'link':link})
	return ret

if __name__ == "__main__":
	print newscraw()