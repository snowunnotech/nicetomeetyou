#!/bin/bash
#===============================================================================
#
#          FILE:  entry_point.sh
#
#         USAGE:  ./entry_point.sh
#
#   DESCRIPTION:  entry point for django project
#
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  Stanley Yuan (), None
#       COMPANY:  None
#       VERSION:  1.0
#       CREATED:  06/08/2019 09:57:13 PM CST
#      REVISION:  ---
#===============================================================================

python -m news.helpers.scrapy
python manage.py runserver 0.0.0.0:8000
