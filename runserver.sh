#!/bin/bash

#Program:
# start nginx service and run uwsgi

# under pipenv

#setting env
export DJANGO_SETTINGS_MODULE=NBA.settings.pro

#run server
sudo service nginx restart
uwsgi --ini NBA/config/uwsgi.ini


