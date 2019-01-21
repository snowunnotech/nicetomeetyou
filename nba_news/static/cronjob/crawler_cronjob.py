import requests

def update_news_list():
    api_url = "http://localhost:8000/update_news_data"
    res = requests.get(api_url)
    if res.status_code != 200:
        print("Update Failed")

if __name__ == "__main__":
    update_news_list()
