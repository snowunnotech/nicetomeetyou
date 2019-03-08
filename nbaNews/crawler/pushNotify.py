import requests


class PushNotify:
    def __init__(self, token):
        url = 'https://web-push-codelab.glitch.me/api/send-push-msg'
        headers = {
            'Content-Type': 'application/json'
        }
        data = '''
            ,
            "data": "ffsdafdsfg",
            "applicationKeys": {
                "public": "BGz7BFftYii-12iSSe1U6PxSsYJ8zOzr5o7iyJAq67O5DcrEpSBtZsIj7IjP9oOfI1xqAE664DIyhW7iTKAXtoI",
                "private": "HeEHWRcZCiECNb2P_hrFEYF_tmC960d2Ob6PC43mL-8"
            }
        }
        '''


        data = '{"subscription": ' + token + data
        res = requests.post(url, headers=headers, data=data)


    def run(self):
        return
# https://developers.google.com/web/fundamentals/codelabs/push-notifications/?hl=zh-tw
# https://web-push-codelab.glitch.me/
if __name__ == '__main__':
    token = '''
            {
                    "endpoint": "https://fcm.googleapis.com/fcm/send/fRbj7k6grVQ:APA91bEZzi3Pw2YvsAEvsm4UiBfCr_doGI7lTd10kYo0_evu3gnuhmfJEt34tkOGtnsXrq6j66IMDyemUYGYtyE7CaursqhozRbw7_874lJsey6wmhdBYUKPmBGWS8xb_i8Y1ACGIuOx",
                    "expirationTime": null,
                    "keys": {
                        "p256dh": "BD3Qjfd0frodm1zDfAFKT-MJNhjcuw5Z5STmT_j1HgV0X_RkwdVmXly6h1YfT0PAVuwCh36655qIkDfeeC2ZYpU",
                        "auth": "gqk5YNVbsObH0gMbjlDAqQ"
                    }
                }
            '''
    PushNotify(token)
