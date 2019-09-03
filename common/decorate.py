from django.http import JsonResponse
from functools import wraps


def api_json(func):
    @wraps(func)
    def _func(*args, **kwargs):
        json_obj = func(*args, **kwargs)
        return JsonResponse(json_obj)
        # return json_obj
    return _func


# 測試程式碼執行，在被匯入其他檔案中時下面程式碼不會起作用
if __name__ == '__main__':
    @api_json
    def hello():
        return {'name': 'zhangsan'}
    print(hello())