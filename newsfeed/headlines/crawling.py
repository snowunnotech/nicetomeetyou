import requests
import re

from bs4 import BeautifulSoup as bs

r = requests.get('https://nba.udn.com/nba/cate/6754')
content = r.text
