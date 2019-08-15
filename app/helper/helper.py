import random, string
# from django.conf import settings
from rest_framework.response import Response

class APIHandler:
    @staticmethod
    def catch(data, code):
        return Response({'code': 'S001'+code, 'data': data})