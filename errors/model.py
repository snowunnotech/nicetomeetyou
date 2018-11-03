# -*- coding: utf-8 -*-

def get_not_news_found_error(id):
    not_news_found_error = {
        'id': id,
        'error_msg': '新聞找不到'
    }

    return not_news_found_error

def get_found_duplicated_news_error():
    found_duplicated_news_error = {
        'error_msg': '有重複新聞'
    }

    return found_duplicated_news_error