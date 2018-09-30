"""
Command-line utility for administrative tasks.
"""
import os
import sys
import threading
import time
import socket
import requests

def circlecrawler():
  time.sleep(5)
  while 1==1:     
      r = requests.get('https://localhost:'+str(sys.argv[-1]) +'/api/getclecrawler' )
      print(r.text)
      time.sleep(60*5)
          
number = sys.argv[-1].isdigit()
if number:
    t = threading.Thread(target = circlecrawler)
    t.start()


if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "nicetomeetyou.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
