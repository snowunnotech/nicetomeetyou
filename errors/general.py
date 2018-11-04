# -*- coding: utf-8 -*-

def get_other_error():
    other_error = {
        'error_msg': '錯誤'
    }

    return other_error

# 錯誤處理，在這裡這有印出功能
def error_handler(e):
    e.with_traceback()
    print(e)