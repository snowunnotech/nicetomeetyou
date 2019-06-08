""" This modules contains the class for get response from website"""

import requests

class Scraper:
    "For get response from the target website"

    def __init__(self, url="www.google.com"):
        self.url = url
        self.request_headers = None
        self.response = None
        self.text = None
        self.request_data = None

    def create_request_data(self):
        "Init request data"
        data = {
            'gr': 'ww'
        }

        self.request_data = data

        return data

    def create_request_headers(self):
        "Init request headers"
        headers = {
            "authority": "nba.udn.com",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/73.0.3683.75 Safari/537.36",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        self.request_headers = headers

        return headers

    def request(self):
        "Get response from target url"
        response = requests.get(self.url, params=self.request_data)
        self.response = response

        return response

    def get_response_text(self, response=None):
        "Get text of response"
        if response is not None:
            text = response.text
        else:
            text = self.response.text

        self.text = text

        return text

    def run(self):
        "Run the whole request process and return text"
        self.create_request_headers()
        self.create_request_data()
        self.request()
        text = self.get_response_text()

        return text


if __name__ == "__main__":
    pass
