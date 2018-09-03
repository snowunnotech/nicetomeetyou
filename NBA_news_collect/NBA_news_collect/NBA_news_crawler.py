import re
import requests
from bs4 import BeautifulSoup
import sqlite3
import lxml











class NBA_news_crawler():
	
	def __init__(self):
		self.web_url = "https://nba.udn.com"
	


	def store_news_info(self):

		#獲取新聞頁面資訊並找到包含焦點新聞資訊的<dt>標籤
		r = requests.get("https://nba.udn.com/nba/index?gr=www")
		soup_of_list = BeautifulSoup(r.text, "lxml")
		tag_dt = soup_of_list.find("div", id = "news_body").find_all("dt", limit = 3) 

		#獲得焦點新聞資訊並存入資料庫
		for html in tag_dt: 
			#獲得焦點新聞列表頁面資訊
			title = html.find("h3").text
			detail_path = html.find("a")["href"]
			detail_url = f"{self.web_url}{detail_path}"
			image_url = html.find("img")["src"]
		

			
			#獲得焦點新聞內容頁面資訊
			r = requests.get(detail_url)
			soup_of_detail = BeautifulSoup(r.text, "lxml")


			bar = soup_of_detail.find(class_="shareBar__info--author")
			post_date = bar.find("span").text
			author = bar.text.replace(post_date, "")
			p_detail = soup_of_detail.find(id="story_body_content").find_all("p")[1:]
			detail = "\n".join([p_content.text for p_content in p_detail]).replace('\'', '`')
			video_url = soup_of_detail.find(class_="video-container").find("iframe")["src"]

					
			#將新聞資訊存放於字典中
			news_info_dict = {
									"title": title,
									"image_url": image_url,
									"detail_url": detail_url,
									"post_date": post_date,
									"author": author,
									"detail": detail,
									"video_url": video_url,




							}
			#將新聞資訊字典存入資料庫
			#連接資料庫並檢查資料是否已存在資料庫					
			conn = sqlite3.connect("db.sqlite3")
			sql_cmd = "SELECT title, post_date FROM News_news WHERE title='{0}' AND post_date='{1}'"
			sql_cmd = sql_cmd.format(news_info_dict['title'], news_info_dict['post_date'])
			exists = conn.execute(sql_cmd).fetchall()
			if not exists:
				#若資料庫無新聞資料則將之存入資料庫中，完成後關閉與資料庫的連接
				sql = "INSERT INTO News_news (title, image_url, detail_url, post_date, author, detail, video_url) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}' )"
				sql = sql.format(news_info_dict['title'], news_info_dict['image_url'], news_info_dict['detail_url'], news_info_dict['post_date'], news_info_dict['author'], news_info_dict['detail'], news_info_dict['video_url'])
				print(sql)
				cursor = conn.execute(sql)
				print(cursor.rowcount)
				conn.commit()
				conn.close()
			
		
						
if __name__ == '__main__':
	NBA_news_crawler().store_news_info()


