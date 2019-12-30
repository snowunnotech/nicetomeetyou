from bs4 import BeautifulSoup
import requests
import html5lib
def get_web(url):
	web = requests.get(url)
	if web.status_code == 200:
		return web.text
	else:
		return "出現錯誤囉!!"
def get_more_page(web_content, data ,counter):
	all_dt = web_content.find("div", id="news_list_body").find_all("dt")
	last_page =  "https://nba.udn.com" + web_content.find("div",class_="pagelink").find("gonext").find("a")["href"]
	for row in all_dt:
		href = "https://nba.udn.com" + row.find("a")['href']
		title = row.find("a").find("h3").text
		data.append({
			"href": href,
			"title": title
		})
	if counter > 0:
		counter = counter - 1
		web = get_web(last_page)
		web_content = BeautifulSoup(web, 'html5lib')
		data = get_more_page(web_content, data, counter)
	return data
def main():
	web = get_web("https://nba.udn.com/nba/cate/6754")
	web_content = BeautifulSoup(web , 'html5lib')
	data = [] ; counter = 10 ;  # 抓前10頁
	data = get_more_page(web_content, data, counter)
	return data

if __name__ == '__main__':
	main()