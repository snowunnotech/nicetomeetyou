# -*- coding: utf-8 -*-
import json
import requests

def import_to_website(news):
    news_json = json.dumps(news)
    try:
        req = requests.post('http://127.0.0.1:8000/import_news/', data={'news_json': news_json})
        msg = json.loads(req.text)
        if 'error_msg' in msg.keys():
            print('import failed:' + news['news_url'])
        else:
            print('import done:' + news['news_url'])
    except Exception as e:
        print(e)
    finally:
        pass