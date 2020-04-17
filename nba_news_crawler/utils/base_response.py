from enum import Enum
from django.http import JsonResponse


class StatusType(Enum):
    SUCCESS = 200
    WRONG_REQUEST = 500
    WRONG_METHOD = 405


class Response(JsonResponse):
    def __init__(self, json, status_code=StatusType.SUCCESS, **kwargs):
        response = {
            "data": json
        }
        JsonResponse.__init__(self, response, status=status_code.value, **kwargs)
