from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import os
import json
import subprocess
import sqlite3
import pandas as pd


class index(APIView):
	def __init__(self):
		self.INDEX_VAR = {}
		pass
	def get(self , request,*args,**kwargs):
		return render(request,os.path.join('.','index.html'),self.INDEX_VAR)

class news_api(APIView):
	def __init__(self):
		ALL_TABLES_SQL = """SELECT name
			FROM sqlite_master 
			WHERE type ='table' AND 
			name NOT LIKE 'sqlite_%';"""

		self.API_RETURN_SQL = """
			SELECT *
			FROM {_table}
			ORDER BY `datetime` DESC;"""

		self.conn = sqlite3.connect('scrapy.db')
		self.cur = self.conn.cursor()
		self.cur.execute(ALL_TABLES_SQL)
		self.ALL_TABLES = [_val[0] for _val in self.cur.fetchall()]


	def post(self , request,*args,**kwargs):
		if kwargs.get('news_name',"") in self.ALL_TABLES:
			df_result = pd.read_sql(self.API_RETURN_SQL.format(_table = kwargs.get('news_name',"")),self.conn)
			return JsonResponse(json.loads(df_result.to_json(orient='records')), safe=False)
		else:
			return HttpResponse("<h1>%s</h1>" % ("Not found data"))