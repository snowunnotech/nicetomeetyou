#!/bin/bash
#===============================================================================
#
#          FILE:  init.sh
#
#         USAGE:  ./init.sh
#
#   DESCRIPTION:  init django project
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

cd /code && \
  python3 manage.py makemigrations && \
  python3 manage.py migrate
