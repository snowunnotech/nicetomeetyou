from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ContentCrawlerTests(APITestCase):
    def test_content_crawler(self):
        """
        Ensure we can get news content.
        """
        url = '/crawler/news_content/'
        data = {
            "url":"https://nba.udn.com/nba/story/6780/3303502"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,
                         {
                             "status": "ok",
                             "description": "get news content successfully",
                             "author": "2018-08-11 14:19NBA台灣 / udn記者陳元廷／綜合外電報導",
                             "content": "NBA\nfacebook\ntwitter\npinterest 7月份在奧克蘭的捷運系統發生一起駭人聽聞命案，1位白人男子疑似隨機持刀攻擊數位黑人女乘客，最後造成1位名為妮娜（Nia Wilson）的18歲非裔少女不幸身亡。  此案也在NBA球員間產生極大震撼，其中拓荒者後衛里拉德（Damian Lillard）因為出身當地感受特別深，他表示：「假如今天送命的是我的孩子呢？她才18歲，而且她什麼事也沒做，我過去常常也搭捷運四處跑，裡頭總是擠滿了人，真的很難料到會出什麼事。」  至於身為灣區代表球星的柯瑞（Stephen Curry）則是透過自己的慈善基金會，以舉辦公益表演賽形式協助受害者家屬募款，柯瑞對此透露：「我相信每個人都意識到這樁慘案，這真的是一件慘無人道的事，我希望把這場比賽獻給妮娜一家，為你們的堅強獻上最高敬意。」  妮娜父親也發表聲明感謝柯瑞支持，其中提到：「正是有了柯瑞還有來自各界的支持，我們一家才得以堅強度過這個難關，是你們讓我們在這時刻依然支撐住自己。」  "
                         })

    def test_content_crawler_error_url(self):
        """
        get error url
        """
        url = '/crawler/news_content/'
        data = {
            "url":"https://"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'error')
